#Virtual Paint

import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

#to find all different types of colors
# myColors = [[5,107,0,19,255,255],
#             [133,56,0,159,156,255],
#             [57,76,0,100,255,255]]

myColors = [[0,93,133,27,255,255],
            [26,63,0,92,156,255],
            [170,37,124,179,255,255]]

#RGB color codes chart (rapidtables.com)
#make sure you write it in BGR(not RGB)
# myColorValues = [[51,153,255],
#                  [255,0,255],
#                  [0,255,0]]

myColorValues = [[0,128,255],
                 [0,204,0],
                 [153,153,255]]
myPoints = [] ##[x,y,colorId]
#Next is finding colors

def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        # lower = np.array([h_min,s_min,v_min])
        # lower = np.array(myColors[0][0:3])
        lower = np.array(color[0:3])
        # upper = np.array([h_max, s_max, v_max])
        # upper = np.array(myColors[0][3:6])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getContours(mask)
        # cv2.circle(imgResult,(x,y),10,(255,0,0),cv2.FILLED)
        cv2.circle(imgResult, (x, y), 10,myColorValues[count], cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        # cv2.imshow(str(color[0]),mask)
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            # cv2.drawContours(imgResult, cnt, -1, (255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y


def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10, myColorValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors, myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)


    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


