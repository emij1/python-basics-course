from cv2 import cv2
import numpy as np
import sys
import os

# Setting the image name

#image_filename = input("Enter the name of the image you want to process.\nThe image has to be in the same directory as this script: ")

image_filename = "sample_coins.jpg"

# Getting the file path for image relative to the script
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

path = os.path.join(__location__, image_filename)

# Reading image and storing it in a variable

original_image = cv2.imread(path)
cv2.imshow("Original image", original_image)
cv2.waitKey(0)

# Transforming image into grayscale version

grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Reducing noise in image using GaussianBlur

GaussValue = 3

gaussBlur_image = cv2.GaussianBlur(grayscale_image, (GaussValue, GaussValue), 0)

# Using Canny function to remove noise even further and find borders

canny_image = cv2.Canny(gaussBlur_image, 60, 100)

# Morphing noise inside outer contours to ignore shapes inside

KernelValue = 3

kernel = np.ones((KernelValue,KernelValue),np.uint8)
closing_image = cv2.morphologyEx(canny_image, cv2.MORPH_CLOSE, kernel)

# Obtaining threshold image

# Finding contours to identify coins
# Use .copy() on closing_image
contours, hierarchy = cv2.findContours(closing_image.copy() , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Coins found: {}".format(len(contours)))

image_with_contours = cv2.imread(path)
cv2.drawContours(image_with_contours,contours,-1, (0,0,255), 2)

cv2.imshow("Image with detected coins", image_with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
