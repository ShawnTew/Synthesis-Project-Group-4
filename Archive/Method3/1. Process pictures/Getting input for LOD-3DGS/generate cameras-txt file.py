import pandas as pd

input_cubemap_imagestxt = 'cameras_colmap.txt'
output_cameras_txt = 'cameras.txt'

camera_params = pd.read_csv(input_cubemap_imagestxt, sep='\s+', header=None)
camera_params = camera_params.iloc[3:].reset_index(drop=True)
width = camera_params[2].astype(float).mean()
height = camera_params[3].astype(float).mean()
focal_length = camera_params[4].astype(float).mean()
principal_point_x = camera_params[5].astype(float).mean()
principal_point_y = camera_params[6].astype(float).mean()
params = camera_params[7].astype(float).mean()

with open(output_cameras_txt, 'w') as f:
    f.writelines(f'1 PINHOLE {int(width)} {int(height)} {focal_length} {int(principal_point_x)} {int(principal_point_y)} {params}')