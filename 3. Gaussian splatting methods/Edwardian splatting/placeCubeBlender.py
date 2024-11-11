import bpy
import csv

# Define the path to your CSV file
csv_file_path = ""

# Open the CSV file and read the coordinates
with open(csv_file_path, mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    # Assuming the CSV contains three columns: X, Y, Z
    for row in csv_reader:
        # Convert the row values to floats
        x, y, z = map(float, row)
        
        # Create a new cube mesh
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(x, y, z))
        
        # Optionally, scale the cube down if you want smaller cubes
        bpy.context.object.scale = (0.01, 0.01, 0.01)

print("Cubes placed at coordinates from CSV!")