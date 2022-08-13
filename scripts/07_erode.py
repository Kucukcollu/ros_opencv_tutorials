# Python program to explain cv2.erode() method

# importing cv2
import cv2

# importing numpy
import numpy as np

# Reading an image in default mode
image = cv2.imread("../images/image.png")

# Creating kernel
kernel = np.ones((5, 5), np.uint8)

# Using cv2.erode() method
image = cv2.erode(image, kernel)

# Displaying the image
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()