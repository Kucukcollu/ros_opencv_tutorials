
# Python program to explain cv2.imwrite() method
  
# importing cv2 
import cv2
  
# Using cv2.imread() method
# to read the image
img = cv2.imread("../images/image.png")
  
# Filename
filename = "../images/saved_image.jpg"
  
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, img)
  
print('Successfully saved')