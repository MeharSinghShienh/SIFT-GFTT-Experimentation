import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
image = cv2.imread("Waterloo_Field_Overview-1.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges using Canny edge detection
edges = cv2.Canny(blurred, threshold1=150, threshold2=350)

# Show the edge
plt.imshow(edges, cmap="gray")
plt.axis("off")
plt.show()

# Apply Hough Line Transform
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 180, threshold=80, minLineLength=50, maxLineGap=10)

# Create an empty image to draw the lines
line_image = np.zeros_like(image)

# Draw the detected lines
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(line_image, (x1, y1), (x2, y2), (255, 255, 255), thickness=5)  # White lines

# Show the detected lines
plt.imshow(cv2.cvtColor(line_image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

