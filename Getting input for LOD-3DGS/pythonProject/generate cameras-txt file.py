import math

# Image width and FoV for forward lens
width = 1907 - 67
height = 1896 - 56
image_width = 1840

fov_degrees = 200.188694239822

# Convert FoV to radians
fov_radians = math.radians(fov_degrees)

# Calculate focal length
focal_length = image_width / (2 * math.tan(fov_radians / 2))

# Camera parameters
camera_id = 1
camera_model = "PINHOLE"
image_width = 960
image_height = 960
cx = 480.0
cy = 480.0

output_camera_lines = []

# Define one camera for each face (Front, Left, Right, Up, Down)
for face in ['F', 'L', 'R', 'U', 'D']:
    output_camera_line = f"{camera_id} {camera_model} {image_width} {image_height} {focal_length} {focal_length} {cx} {cy}\n"
    output_camera_lines.append(output_camera_line)
    camera_id += 1

# Write to cameras.txt
with open('cameras.txt', 'w') as f:
    f.writelines(output_camera_lines)

print("cameras.txt file generated successfully!")


output_lines = [f'1 PINHOLE {image_width} {image_width} {focal_length} {focal_length} 920 920']

with open('cameras.txt', 'w') as f:
    f.writelines(output_lines)
