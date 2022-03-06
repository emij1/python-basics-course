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

# Defining function to show each image processing step

def showStep(description, imageView):
    cv2.imshow(description,imageView)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Reading image and storing it in a variable

original_image = cv2.imread(path)
showStep("Original image", original_image)

# Transforming image into grayscale version

grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
showStep("Grayscale version", grayscale_image)

# Reducing noise in image using GaussianBlur

GaussValue = 3
KernelValue = 3

gaussBlur_image = cv2.GaussianBlur(grayscale_image, (GaussValue, GaussValue), 0)
showStep("Image with reduced noise", gaussBlur_image)

# Obtaining threshold image

__, threshold_image = cv2.threshold(gaussBlur_image,140,255,cv2.THRESH_BINARY_INV)
showStep("Threshold Binary version", threshold_image)

# Using Canny function to remove noise even further and find borders

canny_image = cv2.Canny(threshold_image, 60, 100)
showStep("Canny image", canny_image)

#
kernel = np.ones((KernelValue,KernelValue),np.uint8)
closing_image = cv2.morphologyEx(canny_image, cv2.MORPH_CLOSE, kernel)
showStep("Closing Image", closing_image)


# Finding contours to identify coins
# Use .copy() on closing_image
contours, hierarchy = cv2.findContours(closing_image.copy() , cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Coins found: {}".format(len(contours)))

image_with_contours = cv2.imread(path)
cv2.drawContours(image_with_contours,contours,-1, (0,0,255), 2)

showStep("Image with detected coins", image_with_contours)