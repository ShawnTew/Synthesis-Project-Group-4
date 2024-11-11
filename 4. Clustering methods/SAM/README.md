# Segment Anything Model (SAM)

The **Segment Anything Model (SAM)** is an advanced segmentation model capable of segmenting various types of data, including images, point clouds, and Gaussian splats. SAM leverages state-of-the-art techniques in computer vision and machine learning to provide flexible and high-quality segmentation across diverse data formats. 

This implementation focuses on two specific applications: segmenting point clouds and Gaussian splats. By applying SAM to these data types, users can achieve fine-grained segmentation that can be used for visualization, analysis, or further data processing.

The full guide to this workflow can be referenced [here](https://towardsdatascience.com/segment-anything-3d-for-point-clouds-complete-guide-sam-3d-80c06be99a18).


## Abstract
This folder contains files for performing SAM-based segmentation on both point clouds and Gaussian splats. Each type of segmentation is handled in a separate Jupyter notebook:
- **Point Cloud Segmentation**: Available in *SAM_PC.ipynb*
- **Gaussian Splat Segmentation**: Available in *SAM_GS.ipynb*

## Steps
1. Set up an environment with the following dependencies: `numpy`, `matplotlib`, `cv2`, `laspy`, `open3d`, and `plyfile`.
2. Replace the placeholder file paths in each notebook with the paths to your specific files.
3. Run the notebooks as needed.

Segmented results will be saved in the folder *7. Results*.
