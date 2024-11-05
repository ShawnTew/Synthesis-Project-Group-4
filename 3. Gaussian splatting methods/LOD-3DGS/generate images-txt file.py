import pandas as pd
import numpy as np
import os

trajectory_data = pd.read_csv('../../1. Data/geoslam/traj.txt', sep='\s+', header=0)
camera_data = pd.read_csv('../../1. Data/geoslam/orbit_import_camera.csv')
input_folder_cubemap_images = '../../7. Results/cube map images'
output_images_txt = 'images.txt'

class Quaternion:
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        w1, x1, y1, z1 = self.w, self.x, self.y, self.z
        w2, x2, y2, z2 = other.w, other.x, other.y, other.z

        w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
        x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
        y = w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2
        z = w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2

        return Quaternion(w, x, y, z)

    def __repr__(self):
        return f"Quaternion(w={self.w}, x={self.x}, y={self.y}, z={self.z})"

    def normalize(self):
        norm = np.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)
        return Quaternion(self.w / norm, self.x / norm, self.y / norm, self.z / norm)

    def get_view_quaternion(self, view, angle=90):
        theta_y = np.radians(angle)
        theta_x = np.radians(angle)

        q_y_R = Quaternion(np.cos(-theta_y / 2), 0, np.sin(-theta_y / 2), 0).normalize()
        q_y_L = Quaternion(np.cos(theta_y / 2), 0, np.sin(theta_y / 2), 0).normalize()

        q_y_B = Quaternion(np.cos(-theta_x / 2), np.sin(-theta_x / 2), 0, 0).normalize()
        q_y_F = Quaternion(np.cos(theta_x / 2), np.sin(theta_x / 2), 0, 0).normalize()

        q_top = Quaternion(0, 1, 0, 0)

        q_down_n = Quaternion(self.w, self.x, self.y, self.z).normalize()

        if view == 'F': #Front
            return q_y_F * q_down_n
        elif view == 'B': #Back
            return q_y_B * q_down_n
        elif view == 'R': #Right
            return q_y_R * q_down_n
        elif view == 'L': #Left
            return q_y_L * q_down_n
        elif view == 'T' or view == 'U': #Top
            return q_top * q_down_n
        elif view == 'D': #Down
            return q_down_n
        else:
            return q_down_n


output_lines = []

index_image = -1
for index, row in camera_data.iterrows():
    image_id = row['Id']
    image_filename_base = row[' Image'].strip()
    time_stamp = row[' Time']

    views = []
    for image_file in os.listdir(input_folder_cubemap_images):
        if image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_folder_cubemap_images, image_file)
            image_name = os.path.splitext(image_file)[0]
            if image_name[:-2] == image_filename_base[:-4]:
                views.append(image_name[8])
                index_image += 1
    views_per_image = len(views)

    world_time_col = trajectory_data.columns[0]
    matching_trajectory = pd.DataFrame()

    for i, time in enumerate(trajectory_data[world_time_col]):
        if abs(time_stamp - time) < 0.01:
            matching_trajectory = trajectory_data.iloc[i]

    if not matching_trajectory.empty:
        x = matching_trajectory['x']
        y = matching_trajectory['y']
        z = matching_trajectory['z']
        q0 = matching_trajectory['q0']
        q1 = matching_trajectory['q1']
        q2 = matching_trajectory['q2']
        q3 = matching_trajectory['q3']
        down_quat = Quaternion(q0, q1, q2, q3)

        for j, view in enumerate(views):
            q_view = down_quat.get_view_quaternion(view)
            output_line = (f"{index_image} {q_view.w} {q_view.x} {q_view.y} {q_view.z} {x} {y} {z} "
                               f"1 {image_filename_base[:-4]}_{view}.jpg\n")
            output_lines.append(output_line)
            output_lines.append(" No Content \n")

with open(output_images_txt, 'w') as f:
    f.writelines(output_lines)

print("images.txt file generated successfully!")