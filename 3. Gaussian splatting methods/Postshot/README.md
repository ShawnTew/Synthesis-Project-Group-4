# Jawset PostShot

## Abstract
**PostShot** is a Gaussian splatting tool with a built-in graphical user interface designed for 3D rendering and visualization. It leverages [Gaussian Splatting](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) in conjunction with neural radiance fields to render detailed and high-quality splats.

## Installation
To install Jawset PostShot, visit the [official site](https://www.jawset.com/) and download the installer. Run the `.exe` file to complete the installation process.

## Usage
PostShot allows users to input data in various formats, providing flexibility for different projects. Supported inputs include:
1. **Images Only**
2. **Images + Camera Poses (.txt)**
3. **Images + Camera Poses (.txt) + Sparse Point Cloud**

Once an input type is selected, users can configure Gaussian splatting parameters such as:
- **Maximum Training Samples**: Set a limit for training sample volume.
- **Maximum Number of Splats**: Define the cap for splats to control rendering density.

Fine-tuning these settings can optimize the rendering for performance or quality based on project needs.
