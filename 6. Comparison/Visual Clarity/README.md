# Laplacian Filter for Sharpness Detection

This script applies a Laplacian filter to an image, ignoring specific white areas, to measure the sharpness score based on the variance of the Laplacian result. This is useful for evaluating the clarity or blur in an image, especially when certain areas need to be excluded from the analysis.

## Steps

1. **Load and Convert Image**: The script reads an image in color, converts it to grayscale, and applies a mask to ignore specific background colour.
2. **Apply Laplacian Filter**: The masked grayscale image undergoes a Laplacian filter transformation to highlight areas with rapid intensity changes (edges).
3. **Calculate Sharpness Score**: The variance of the filtered image is calculated to quantify sharpness, only including areas that are not white.
4. **Save and Visualize**: The script saves both the grayscale and Laplacian-filtered images and displays them side by side for visual comparison.

## Installation

To run this code, you need Python with the following libraries:
- OpenCV
- NumPy
- Matplotlib

You can install these dependencies using pip:

`pip install opencv-python numpy matplotlib`

## Configuring and Running the Script

### Set the Image Path

1. In the script, locate the following line:

   `image_path = 'Comparison_image_revit.png'  # Replace with your image path`

2. Replace `'Comparison_image_revit.png'` with the path to your own image file. This should be the path of the image you want to analyze.

### Specify the Background Color to Ignore

The script is set to ignore areas with an RGB color `[102, 102, 102]` in the image. If you want to ignore a different color, locate this line in the code:

`mask = np.all(image_color != [102, 102, 102], axis=-1)`

Replace `[102, 102, 102]` with the RGB values of the background color you want to ignore. For example, to ignore pure white areas, change it to `[255, 255, 255]`.

### Run the Script

With these adjustments made, you can run the script by executing:

`python Laplacian.py`

## Output

### Sharpness Score
Printed in the terminal, based on the variance of the Laplacian filter applied to the masked grayscale image. This score represents the image's sharpness in non-background areas.

### Saved Images
- `SPLAT_image_grayscale.png`: The masked grayscale version of your input image, with the background areas excluded.
- `SPLAT_laplacian_image.png`: The result of the Laplacian filter applied to the masked grayscale image, highlighting edges in relevant regions.

These saved images provide a visual representation of which areas are analyzed and the effect of the Laplacian filter.