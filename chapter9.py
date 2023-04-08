#Face Detection

import cv2
import numpy as np

#there are so many cascades in opencv which you can directly use instead of training and testing the faces and non-faces
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/Screenshot.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Result",img)
cv2.waitKey(0)

cam = cv2.VideoCapture(0)
#id 3 is width
cam.set(3,640)
#id 4 is height
cam.set(4,480)
# id 10 for brightness
cam.set(10,100)
while True:
    success, img2 = cam.read()
    img2Gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    faces2 = faceCascade.detectMultiScale(img2,1.1,4)
    # faces = faceCascade.detectMultiScale(img2Gray, 1.1, 4)
    for (x, y, w, h) in faces2:
        cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Video",img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break