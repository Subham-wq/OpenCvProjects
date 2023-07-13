import os
import cv2

# Path to the folder containing the images
folder_path = #folder path

# Lists to store the widths and heights
widths = []
heights = []

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    # Construct the full path to the image file
    image_path = os.path.join(folder_path, filename)

    # Load the image
    image = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if image is not None:
        # Get the height and width of the image
        height, width, _ = image.shape

        # Append the width and height to the respective lists
        widths.append(width)
        heights.append(height)
    else:
        print(f"Failed to load the image: {filename}")
