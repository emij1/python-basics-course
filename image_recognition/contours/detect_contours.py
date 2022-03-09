from cv2 import THRESH_BINARY, cv2
import sys
import os

# Setting the image name

image_filename = input("Enter the name of the image you want to process.\nThe image has to be in the same directory as this script: ")
image_filename = "cura-icon.jpg"

# Getting the file path for image relative to the script
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

path = os.path.join(__location__, image_filename)

# Reading image and storing it in a variable

original_image = cv2.imread(path)

# Cleaning up the name of the file for the next Window pop-up

window_name = image_filename.replace("-"," ").replace(".jpg","").capitalize()

# Transforming stored image into grayscale

grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Obtaining the threshold image

__, threshold_image = cv2.threshold(grayscale_image, 220, 255, cv2.THRESH_BINARY_INV)

# Identifying contour

contours, hierarchy = cv2.findContours(threshold_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Drawing contours over the original image

image_with_contours = cv2.imread(path) # Storing original image again in different variable for output image, to prevent overwriting the original_image variable

cv2.drawContours(image_with_contours, contours, -1, (0, 0, 255),2)

# Showing image in a pop-up

cv2.imshow(window_name, original_image)
cv2.waitKey(0)
cv2.imshow(window_name, grayscale_image)
cv2.waitKey(0)
cv2.imshow(window_name, threshold_image)
cv2.waitKey(0)
cv2.imshow(window_name, image_with_contours)
cv2.waitKey(0)

cv2.destroyAllWindows()
