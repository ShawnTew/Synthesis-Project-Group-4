# Abstract
This folder contains various scripts and tools designed to process, align, and visualize point clouds and 3D models, as well as extract point clouds from images using different photogrammetry software. The tools support several formats, including PLY and LAS, and employ multiple software packages for 3D reconstruction, segmentation, and visualization. Below is an overview of each script and setup file, along with instructions for installation and usage.

## 1. Point Cloud Alignment and Visualization Script
### Overview
This script handles loading, transforming, aligning, and visualizing multiple point cloud datasets from different sources, including PLY and LAS files. It preserves all attributes and comments from the original files and allows for customizable scaling options during transformation.

### Features
File Support: Loads PLY and LAS files, with attribute preservation.
Error Handling: Reports errors, such as memory issues.
Transformation Computation: Computes rotation, scaling, and translation to align point clouds based on corresponding points.
Visualization: Distinguishes each point cloud with unique colors for easy comparison.
Data Saving: Saves transformed point clouds with original attributes and comments.
Requirements
Python 3.x with the following packages:
```
pip install open3d numpy plyfile laspy
```
### Usage
Update File Paths: Edit paths to your PLY and LAS files in the script.
Define Corresponding Points: Set coordinates for corresponding points between source and target clouds.
Run the Script:
```
python point_cloud_alignment.py
```
## 2. COLMAP Setup
### Overview
COLMAP is a Structure-from-Motion (SfM) software used to create sparse point clouds from image sets. It’s useful for applications requiring Gaussian splatting or other 3D reconstruction techniques.

### Requirements
Hardware: NVIDIA graphics card with CUDA support.
Software: CUDA version 11.x.
### Installation
Download COLMAP from COLMAP Releases.
Extract the downloaded ZIP file and add the path to your system's environment variables.
### Usage
Start COLMAP by clicking on COLMAP.bat.
Use the GUI to perform "Automatic Reconstruction" by specifying folders for "Workspace," "Mask," and "Image."

## 3. CubeMap Setup
### Overview
This tool converts 360-degree fisheye or panoramic images into flat image planes, which are required for COLMAP and Gaussian splatting processes. It’s based on Panorama to Cubemap.

### Requirements
Python Environment (e.g., conda environment with Python 3.12)
Required packages:
```
pip install numpy scipy pillow
```
### Usage
Set the source and output folder paths in the script.
Run the script to process images from the source folder and save the converted cubemap images in the output folder.
## 4. Reality Capture
### Overview
Reality Capture is photogrammetry software that generates high-quality 3D point clouds and meshes from image sets. It is often used for 3D scanning, digital preservation, and creating virtual environments.

### Installation
Download and install Reality Capture from the official website.
Follow the on-screen instructions to complete the installation.
### Usage
Load image sets and optional pre-aligned camera poses or sparse point clouds.
Configure alignment and point cloud generation settings.
Run the processing to obtain aligned images, camera poses, and a point cloud file (.ply) for further analysis.

### Summary
This folder provides tools for:

3D point cloud alignment and transformation (Point Cloud Alignment and Visualization Script)
Point cloud extraction from images using COLMAP and Reality Capture
Converting panoramic images to cubemaps for further 3D reconstruction processing.
Each tool requires specific installations and setup. Follow the individual instructions for each tool and refer to the official documentation where necessary. These scripts collectively support a workflow for acquiring, processing, and visualizing detailed 3D models and point clouds from various data sources.
