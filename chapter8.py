#Contours/Shape detection

import cv2
import numpy as np

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    print(hierarchy)
    for cnt in contours:
        area =  cv2.contourArea(cnt)
        print(area)
        # cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
        #check for the minimum area
        if area>100:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            #calculate the curve length
            peri = cv2.arcLength(cnt,True)
            # print(peri)
            #to get the corner points
            #you can play around with the resolution
            #true because our shapes are closed
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            # print(approx)
            #len gives the idea of what the shape is
            #create object corners
            objCor = len(approx)
            print(objCor)
            x, y, w, h = cv2.boundingRect(approx)
            aspRatio = w / float(h)
            objectType = ""
            if objCor ==3: objectType = "Tri"
            elif objCor == 4:
                if aspRatio >0.95 and aspRatio < 1.05:
                    objectType="Square"
                else:
                    objectType=="Rectangle"
            elif objCor ==5: objectType = "Pentagon"
            elif objCor == 6:
                objectType = "Hexagon"
            elif objCor > 6:
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "Circle"
                else:
                    objectType == "Oval"
            else:objectType="None"
            cv2.rectangle(imgContour, (x,y),(x+w,y+h), (0,255,0),2)
            #lets put some deviation (-10) here
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,1,
                        (0,0,0),2)
            print(len(approx))
path = "Resources/vllCR.png"
img = cv2.imread(path)
imgContour = img.copy()
# imgContour = cv2.resize(imgContour,(700,600))
#convert into greyscale
imgGray = cv2.cvtColor(imgContour,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
# imgBlank = np.zeros_like(img)
#from these edges we are going to find out contours

getContours(imgCanny)

cv2.imshow("Original",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Edge",imgCanny)
cv2.imshow("Contour",imgContour)
cv2.waitKey(0)