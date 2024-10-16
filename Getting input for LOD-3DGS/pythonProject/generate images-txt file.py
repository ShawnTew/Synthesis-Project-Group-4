import pandas as pd
import numpy as np

trajectory_data = pd.read_csv('traj.txt', sep='\s+', header=0)
camera_data = pd.read_csv('orbit_import_camera.csv')

output_lines = []

quaternions = {
    'B': lambda x, y: (1, x, -y),  # Front face
    'R': lambda x, y: (x, -1, -y),   # Right face
    'L': lambda x, y: (-x, 1, -y),   # Left face
    'U': lambda x, y: (-y, -x, 1),    # Top face
    'D': lambda x, y: (y, -x, -1)  # Bottom face
}

def change_translation(X, Y, Z, side):
    if side == 'front':
        return X, Y, Z
    if side == 'up':
        return X, -Z, Y
    if side == 'down':
        return X, Z, -Y
    if side == 'left':
        return -Z, Y, X
    if side == 'right':
        return Z, Y, -X
    if side == 'back':
        return -X, Y, -Z

def change_rotation(qw, qx, qy, qz, side):
    if side == 'front':
        return
    if side == 'up':
        return
    if side == 'down':
        return
    if side == 'left':
        return
    if side == 'right':
        return
    if side == 'back':
        return

# Iterate through each camera frame and match it with the trajectory data
for index, row in camera_data.iterrows():
    image_id = row['Id']
    image_filename_base = row[' Image'].strip()
    time_stamp = row[' Time']

    world_time_col = trajectory_data.columns[0]
    matching_trajectory = pd.DataFrame()

    for i, time in enumerate(trajectory_data[world_time_col]):
        if abs(time_stamp - time) < 0.01:
            matching_trajectory = trajectory_data.iloc[i]

    if not matching_trajectory.empty:
        x = matching_trajectory['x']
        y = matching_trajectory['y']
        z = matching_trajectory['z']

        for j, face in enumerate(quaternions.keys()):
            q0, q1, q2, q3 = quaternions[face]
            output_line = f"{image_id*5+j-5} {q0} {q1} {q2} {q3} {x} {y} {z} 1 {image_filename_base}_{face}.jpg\n"
            output_lines.append(output_line)

# Write to images.txt
with open('images.txt', 'w') as f:
    f.writelines(output_lines)

print("images.txt file generated successfully!")