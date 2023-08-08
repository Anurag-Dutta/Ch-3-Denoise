import numpy as np
import cv2


def resize_image(image, target_size):
    return cv2.resize(image, target_size, interpolation=cv2.INTER_LINEAR)


def psnr(img1, img2):
    # Ensure both images have the same size and number of channels
    if img1.shape != img2.shape:
        raise ValueError("Input images must have the same dimensions and number of channels.")

    # Calculate the Mean Squared Error (MSE) between the two images
    mse = np.mean((img1 - img2) ** 2)

    # If MSE is zero, PSNR is infinity (images are identical)
    if mse == 0:
        return float('inf')

    # Calculate the maximum pixel value (assuming pixel values are in the range [0, 255])
    max_pixel = 255.0

    # Calculate PSNR using the formula: PSNR = 20 * log10(MAX_pixel) - 10 * log10(MSE)
    psnr_value = 20 * np.log10(max_pixel) - 10 * np.log10(mse)

    return psnr_value


# Example usage:
if __name__ == "__main__":
    # Load the images (replace 'image1.jpg' and 'image2.jpg' with your own image filenames)
    img1 = cv2.imread('M3G20090606T093322_V01_L2_8.tif')
    img2 = cv2.imread('M3G20090606T093322_V01_L2_8_HyMiNoR.tif')

    # Resize the images to the same dimensions (choose a common target size)
    target_size = (500, 500)
    img1_resized = resize_image(img1, target_size)
    img2_resized = resize_image(img2, target_size)

    # Calculate PSNR between the two images
    try:
        psnr_score = psnr(img1_resized, img2_resized)
        print(f"PSNR value: {psnr_score:.2f} dB")
    except ValueError as e:
        print(f"Error: {e}")

