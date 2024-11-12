# 3D Model Visualization Tools: Blender and SuperSplat
This folder contains setup guides and usage instructions for two powerful tools used to visualize and work with 3D models, including Gaussian splats, IFC models, and point clouds. Blender and SuperSplat offer unique visualization capabilities for different types of 3D data, making them essential tools for projects that require detailed 3D analysis and rendering.

## 1. Blender Setup
### Overview
Blender is a free, open-source 3D modeling and rendering software that supports a wide range of file types, including Gaussian splats, IFC models, and point clouds. In this project, Blender was used to visualize and compare segmented 3D models, offering flexibility in handling different data formats.

### Requirements
Blender Version: 4.2 or later
Blender Add-ons:
Bonsai: For importing and handling IFC models.
Gaussian Splatting Add-on: Based on the original tool by ReshotAI, slightly modified for visualizing Gaussian splats.
### Supported File Types
.ply: Gaussian splatted point cloud files and standard point clouds.
.ifc: IFC models for architectural and structural representations.
### Installation and Setup
#### Gaussian Splatting Add-on
Download the Gaussian Splatting add-on ZIP file.
Open Blender, go to Edit > Preferences (or press Ctrl + ,), then Get Extensions.
Click Install from Disk, navigate to the downloaded ZIP file, and install.
#### Bonsai Add-on for IFC Models
In Blender, open Edit > Preferences and go to Get Extensions.
Search for "Bonsai" and install it from the search results.
### Steps for Importing and Visualizing Different Data Types
#### Gaussian Splats
Open Blender and remove all default objects.
Go to the 3D Gaussian Splatting menu and click Import Gaussian Splatting.
Select the .ply file with Gaussian splats.
To view splats as ellipses, disable the As point cloud (faster) option.
Switch to Viewport Shading for proper rendering.
#### IFC Models
Open Blender and remove all default objects.
Go to File > Open IFC project and select the .ifc file.
Click Load project to display the IFC model.
#### Point Clouds
Open Blender and remove all default objects.
Go to File > Import > Stanford PLY (.ply) and select the point cloud file.
Use the Shader Editor to set up the material:
Add an Attribute node and connect it to the BaseColor and Emission Color of a Principled BSDF shader.
Set the Attribute name to COL to use the color data in the point cloud.
Switch to Viewport Shading to visualize the point cloud.
## 2. SuperSplat Setup
### Overview
SuperSplat is an online platform for viewing and editing Gaussian splatted files. It provides high-quality rendering, making splats appear very realistic, and is useful for inspecting outputs that might not render accurately in Blender.

### Usage
Upload Gaussian splatted files (e.g., from LOD-3DGS) to SuperSplat.
SuperSplat renders the splats efficiently, providing fast and high-quality visualization.
Use SuperSplat to examine Gaussian splat details that may not be visible in Blender, especially for high-level details.
