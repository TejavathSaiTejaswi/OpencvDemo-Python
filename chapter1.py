# cv2 stands for computer vision
import cv2
import numpy as np

print("Package Imported")

# Read images, videos and webcam
# to read images function called imread
# img = cv2.imread("Resources/Screenshot.png")
img = cv2.imread("Resources/Example1.webp")
#To show the image
cv2.imshow("Output:",img)
# to add a delay so that we can see
# 0 to wait for infinity
cv2.waitKey(0)
# any value in milliseconds
# here 1000 is for 1 sec
#cv2.waitKey(1000)

#``````````````````````````````````````````````````````````````````````````#

#Create a video capture object

cap = cv2.VideoCapture("Resources/MOVIE.mp4")
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2)
while True:
    success, img = cap.read()
    #If you want to resize
    imgToShow = cv2.resize(img, (720,480))
    cv2.imshow("Video",imgToShow)
    # cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# reading webcam is same as capturing video. The only thing that changes is giving an id instead of path
cam = cv2.VideoCapture(0)
#id 3 is width
cam.set(3,640)
#id 4 is height
cam.set(4,480)
# id 10 for brightness
cam.set(10,100)
while True:
    success, img2 = cam.read()
    cv2.imshow("Video",img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




