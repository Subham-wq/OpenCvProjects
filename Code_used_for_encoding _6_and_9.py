import cv2

# Load the image
image_path = "C:/Users/subha/Downloads/MNIST Images/Image10.png" # Replace with the path to your image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Threshold the image
_, threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Count white pixels in the image
white_pixel_count = cv2.countNonZero(threshold)

# Get image dimensions
height, width = threshold.shape[:2]

# Divide the image vertically
vertical_half_width = width // 2
vertical_left_half = threshold[:, :vertical_half_width]
vertical_right_half = threshold[:, vertical_half_width:]

# Count white pixels in each vertical half
vertical_left_count = cv2.countNonZero(vertical_left_half)
vertical_right_count = cv2.countNonZero(vertical_right_half)

# Divide the image horizontally
horizontal_half_height = height // 2
horizontal_top_half = threshold[:horizontal_half_height, :]
horizontal_bottom_half = threshold[horizontal_half_height:, :]

# Count white pixels in each horizontal half
horizontal_top_count = cv2.countNonZero(horizontal_top_half)
horizontal_bottom_count = cv2.countNonZero(horizontal_bottom_half)

# Calculate the ratios
vertical_ratio = vertical_left_count / vertical_right_count
horizontal_ratio = horizontal_top_count / horizontal_bottom_count

# Print the results
print("Total White Pixels:", white_pixel_count)
print("Ratio of horizontal white pixels to vertical white pixels:")
print("Vertical Ratio:", vertical_ratio)
print("Horizontal Ratio:", horizontal_ratio)
