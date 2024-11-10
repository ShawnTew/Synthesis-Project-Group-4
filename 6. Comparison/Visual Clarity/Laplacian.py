import cv2
import numpy as np
import matplotlib.pyplot as plt

def save_visualize_laplacian_with_score_ignore_white(image_path):
    # Read the image in color
    image_color = cv2.imread(image_path)
    if image_color is None:
        raise ValueError("Image not found or invalid image format")

    # Convert the image to grayscale
    image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

    # Create a mask to ignore background colour (where all RGB values are 255)
    mask = np.all(image_color != [102, 102, 102], axis=-1)

    # Apply the mask to the grayscale image, setting white areas to zero
    masked_grayscale = np.zeros_like(image_gray)
    masked_grayscale[mask] = image_gray[mask]

    # Apply the Laplacian filter to the masked grayscale image
    laplacian = cv2.Laplacian(masked_grayscale, cv2.CV_64F)

    # Calculate the variance of the Laplacian (sharpness score)
    laplacian_variance = np.var(laplacian[mask])
    print(f"Laplacian Variance (Sharpness Score) ignoring white areas: {laplacian_variance}")

    # Normalize the Laplacian result for saving and visualization
    laplacian_normalized = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX)
    laplacian_normalized = np.uint8(laplacian_normalized)

    # Save the images
    original_image_save_path = 'SPLAT_image_grayscale.png'
    laplacian_image_save_path = 'SPLAT_laplacian_image.png'

    cv2.imwrite(original_image_save_path, masked_grayscale)
    cv2.imwrite(laplacian_image_save_path, laplacian_normalized)

    print(f"Original image saved as: {original_image_save_path}")
    print(f"Laplacian filter output saved as: {laplacian_image_save_path}")

    # Display the images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Masked Grayscale Image")
    plt.imshow(masked_grayscale, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Laplacian Filter Output (Masked)")
    plt.imshow(laplacian_normalized, cmap='gray')
    plt.axis('off')

    plt.show()

# Example usage
image_path = 'Comparison_image_revit.png'  # Replace with your image path
save_visualize_laplacian_with_score_ignore_white(image_path)
