# Generating a Point Cloud in Polycam for Gaussian Splatting
This guide provides instructions on using Polycam to capture a 3D point cloud model, which can be used as input for Gaussian splatting applications. Gaussian splatting is a technique that allows for efficient rendering and visualization of 3D data. Follow these steps to capture, process, and export 3D models using Polycam.

## Prerequisites
### Software
Polycam App: Available for iOS, Android, or via the web at Polycam. Install the app on your device.
Optional Hardware
A mobile device with LiDAR capability (e.g., iPhone Pro models or iPads with LiDAR) for higher-quality scans. Standard mobile cameras also work but may produce lower detail.

## Steps to Generate a Point Cloud in Polycam
1. Capture the Scene or Object
Open the Polycam app and choose the Capture mode.
Use your device's camera to scan the object or scene. Move around to capture multiple angles, ensuring you cover all visible surfaces to get a comprehensive model.
Once you have scanned the entire object or area, end the capture. Polycam will process the images to create a 3D model.
2. Generate the Point Cloud
After capturing the scene, select the Point Cloud option in Polycam to process your capture into a point cloud model.
Allow the app to render the model. You can preview the point cloud to verify that it captures the necessary details.
Adjust Density and Resolution (if available): If the app provides options for point density or resolution, choose the highest settings to ensure a high-quality point cloud suitable for Gaussian splatting.
3. Export the Point Cloud
Export Format: In Polycam, export the point cloud in PLY format. PLY files retain color and attribute information, which are important for visualization in Gaussian splatting.
Download the File: Save the exported PLY file to your computer or desired storage location for further processing.
