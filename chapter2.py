import cv2
import numpy as np

# basic functions required while building opencv projects

# img = cv2.imread("Resources/Screenshot.png")
img = cv2.imread("Resources/Example1.webp")
#convert into grey scale
#cvtColor converts your image into different color spaces
# we use RGB but in opencv the convention is BGR
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Gaussian blur function to blur our image
# we can use original color image or gray image to add the blur
#ksize is the kernel size(it has to be odd numbers)
# sigmax is 0
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

#Edge detector(to find edges in our image) Canny edge detector
#100 is threshold
imgCanny = cv2.Canny(img,100,100)
#to decrease the number of edge detectors
#imgCanny = cv2.Canny(img,150,200)
kernel = np.ones((5,5),np.uint8)
#to increase the thickness of the edge detector
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
#imgDialation = cv2.dilate(imgCanny,kernel.iterations=5)

#to make te edge detector thinner
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)
