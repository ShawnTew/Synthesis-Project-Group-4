# Reality Capture

## Abstract
**Reality Capture** is a photogrammetry software used for creating high-quality 3D point clouds, meshes, and models from images. It enables users to process images for point cloud generation, automatically align images, and retrieve accurate camera poses for further processing or analysis. Reality Capture is widely used for applications such as 3D scanning, digital preservation, and virtual environments.

## Installation
To install Reality Capture, visit the [Reality Capture website](https://www.capturingreality.com/) and download the appropriate version for your system. Follow the on-screen instructions to complete the installation.

## Usage
Reality Capture provides various options for input and settings, enabling precise customization for different types of projects. Supported inputs include:
1. **Image Sets**: Multiple images capturing different angles of the object or scene.
2. **Image Sets + Pre-aligned Camera Poses (optional)**: Load images with a `.txt` file containing pre-aligned camera pose data to optimize alignment.
3. **Image Sets + Sparse Point Cloud (optional)**: Add a `.ply` file with a sparse point cloud to enhance initial alignment and processing accuracy.

After inputting the images, users can configure processing settings such as:
- **Alignment Settings**: Specify parameters for aligning images, like accuracy and tie-point density.
- **Point Cloud Generation**: Control the density of points generated from images for detailed 3D reconstructions.

Once configured, Reality Capture will align images and generate camera poses, which can be exported as a `.txt` file, along with the generated point cloud as a `.ply` file, for further processing.
