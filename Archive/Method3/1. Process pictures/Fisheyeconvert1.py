import os
import cv2
import numpy as np
from PIL import Image

# Set input and output folders
input_folder = "C:\\Users\\ROG\\Desktop\\TU Delft\\Year2\\SYNTHESISPROJECT\\AULA PANAROMIC IMAGES\\panoramas"  # Replace with the folder containing your panoramic images
output_folder = "C:\\Users\\ROG\\Desktop\\TU Delft\\Year2\\SYNTHESISPROJECT\\AULA PANORAMIC IMAGES CUBEMAPED"  # Replace with the folder where the cube map faces will be saved

# Define the cube map face orientations
face_directions = {
    'pz': lambda x, y: (-1, -x, -y),  # Front face
    'nz': lambda x, y: (1, x, -y),    # Back face
    'px': lambda x, y: (x, -1, -y),   # Right face
    'nx': lambda x, y: (-x, 1, -y),   # Left face
    'py': lambda x, y: (-y, -x, 1),   # Top face
    'ny': lambda x, y: (y, -x, -1)    # Bottom face
}

# Normalize vector
def normalize(v):
    norm = np.linalg.norm(v)
    return v / norm if norm > 0 else v

# Convert Cartesian to spherical coordinates
def cartesian_to_spherical(cube):
    r = np.sqrt(cube[0] ** 2 + cube[1] ** 2 + cube[2] ** 2)
    lon = np.arctan2(cube[1], cube[0])  # Longitude
    lat = np.arccos(cube[2] / r)        # Latitude
    return lon, lat

# Function to project the panorama onto a cube face
def render_face(panorama, face, face_size):
    h, w, _ = panorama.shape
    face_img = np.zeros((face_size, face_size, 3), dtype=np.uint8)

    for x in range(face_size):
        for y in range(face_size):
            # Map cube coordinates
            cube_x, cube_y, cube_z = face((2 * (x + 0.5) / face_size - 1), (2 * (y + 0.5) / face_size - 1))
            cube = normalize([cube_x, cube_y, cube_z])

            # Convert cube coordinates to spherical (lat, lon)
            lon, lat = cartesian_to_spherical(cube)

            # Convert spherical coordinates back to panorama coordinates
            src_x = int(((lon + np.pi) / (2 * np.pi)) * w)
            src_y = int((lat / np.pi) * h)

            # Handle bounds
            src_x = np.clip(src_x, 0, w - 1)
            src_y = np.clip(src_y, 0, h - 1)

            # Assign pixel to the face image
            face_img[y, x] = panorama[src_y, src_x]

    return face_img

# Batch processing function
def process_panoramas(input_folder, output_folder, face_size=960):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the folder
    for image_file in os.listdir(input_folder):
        if image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_folder, image_file)
            image_name = os.path.splitext(image_file)[0]
            panorama = cv2.imread(image_path)
            h, w, _ = panorama.shape

            # Create output directory for cube map faces
            output_dir = os.path.join(output_folder, image_name)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            # Generate cube map faces
            for face_name, direction_fn in face_directions.items():
                face_img = render_face(panorama, direction_fn, face_size)
                output_face_path = os.path.join(output_dir, f"{face_name}_face.jpg")
                cv2.imwrite(output_face_path, face_img)

            print(f"Processed cube map for {image_file}")

# Run the batch processing
process_panoramas(input_folder, output_folder)
