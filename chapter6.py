#Joining Images

import cv2
import numpy as np

img = cv2.imread('Resources/Screenshot.png')
#numpy functions(not opencv function)
# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
#The issues with this is we cannot resize the image. It can take whole space.
#the other one is all the images should be of the same number of channels as we are talking about the matrices

# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)
#=================================
#there is a function to solve this(try coding that)

cv2.waitKey(0)