#Color Detection

import cv2
import numpy as np
import os
def empty(a):
    pass
path = "Resources/Example1.webp"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
#Hue min is 0 max can be 179 in opencv
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

# you can get the original wanted color by masking the required part in white and the other things should be in black

# cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
# cv2.createTrackbar("Hue Max","TrackBars",19,179,empty)
# cv2.createTrackbar("Sat Min","TrackBars",110,255,empty)
# cv2.createTrackbar("Sat Max","TrackBars",240,255,empty)
# cv2.createTrackbar("Val Min","TrackBars",153,255,empty)
# cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    img = cv2.imread(path)
    # print(img.shape)
    #create a hsv image
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # define colour values (ranges) (Hue,saturation etc)
    # get trackbar position
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    #instead of black and white to color
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("Original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)
    #you can write the stacking function to collectively view them
    cv2.waitKey(1)