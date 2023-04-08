#Chapter 3 : Resizing and Cropping
#In mathematics the +x axis is towards the east, +y axis is towards the north
#But in opencv the +x axis is towards the east(same), +y axis is towards the south.

import cv2
import numpy as np

img = cv2.imread("Resources/Screenshot.png")
print(img.shape) # 768 is height and 1366 is width

# 300 is width, 200 is height
imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)
# It can't increase the quality, it can increase the pixel size

#next is cropping the image. Cropping can be very useful in getting the information from specific parts of the image
#Image is just a matrix or an array of pixels
# not using opencv function instead matrix functionality itself
# In the above opencv function, it is width and height whereas in matrix it is height and width
imgCropped = img[0:200,200:500]

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)