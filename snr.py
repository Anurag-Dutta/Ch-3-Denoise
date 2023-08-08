import numpy as np
import cv2

def resize_image(image, target_size):
    return cv2.resize(image, target_size, interpolation=cv2.INTER_LINEAR)

def snr(img1, img2):
    # Ensure both images have the same size and number of channels
    if img1.shape != img2.shape:
        raise ValueError("Input images must have the same dimensions and number of channels.")

    # Calculate the difference (noise) between the two images
    noise = img1 - img2

    # Calculate the variance of the noise
    variance = np.var(noise)

    # If variance is zero, SNR is infinity (images are identical)
    if variance == 0:
        return float('inf')

    # Calculate SNR using the formula: SNR = 10 * log10(1 / variance)
    snr_value = 10 * np.log10(1 / variance)

    return snr_value

# Example usage:
if __name__ == "__main__":
    # Load the images (replace 'image1.jpg' and 'image2.jpg' with your own image filenames)
    img1 = cv2.imread('M3G20090606T093322_V01_L2_8.tif')
    img2 = cv2.imread('M3G20090606T093322_V01_L2_8_HyMiNoR.tif')

    # Resize the images to the same dimensions (choose a common target size)
    target_size = (500, 500)
    img1_resized = resize_image(img1, target_size)
    img2_resized = resize_image(img2, target_size)

    # Calculate SNR between the two images
    try:
        snr_score = snr(img1_resized, img2_resized)
        print(f"SNR value: {snr_score:.2f} dB")
    except ValueError as e:
        print(f"Error: {e}")
