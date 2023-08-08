import numpy as np
import cv2

def resize_image(image, target_size):
    return cv2.resize(image, target_size, interpolation=cv2.INTER_LINEAR)

def mae(img1, img2):
    # Ensure both images have the same size and number of channels
    if img1.shape != img2.shape:
        raise ValueError("Input images must have the same dimensions and number of channels.")

    # Calculate the Mean Absolute Error (MAE) between the two images
    mae_value = np.mean(np.abs(img1 - img2))

    return mae_value

# Example usage:
if __name__ == "__main__":
    # Load the images (replace 'image1.jpg' and 'image2.jpg' with your own image filenames)
    img1 = cv2.imread('M3G20090606T093322_V01_L2_8.tif')
    img2 = cv2.imread('M3G20090606T093322_V01_L2_8_HyMiNoR.tif')

    # Resize the images to the same dimensions (choose a common target size)
    target_size = (500, 500)
    img1_resized = resize_image(img1, target_size)
    img2_resized = resize_image(img2, target_size)

    # Calculate MAE between the two images
    try:
        mae_score = mae(img1_resized, img2_resized)
        print(f"MAE value: {mae_score:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
