import os
import cv2

# Path to the folder containing the images
folder_path = r#path

# List to store the total number of white pixels
white_pixels_counts = []

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    # Construct the full path to the image file
    image_path = os.path.join(folder_path, filename)

    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply thresholding to convert the image to binary
    _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

    # Count the number of white pixels
    white_pixels = cv2.countNonZero(binary_image)

    # Append the count to the list
    white_pixels_counts.append(white_pixels)

# Print the list of white pixel counts
print("White pixel counts:", white_pixels_counts)
