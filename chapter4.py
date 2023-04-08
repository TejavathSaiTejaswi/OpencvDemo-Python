#Shapes and Texts

import cv2
import numpy as np

# create a matrix filled with zeros. Zeros means filled with black
#img = np.zeros((512,512)) is a greyscale image
#color functionality, add 3
img = np.zeros((512,512,3),np.uint8)
print(img.shape)
#to color the whole image
#img[:] = 255,0,0

# to create lines we have cv2.line function
#parameters are start point, end point, color, and thickness
# cv2.line(img,(0,0),(300,300),(0,255,0),3)
#img.shape[1]-> width;img.shape[0]-> height
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
#to fill the rectangle
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,255,0),5)

#img-> image;"OPENCV "->text;(300,200)->origin;cv2.FONT_HERSHEY_COMPLEX->font;1->scale;(0,150,0)->color;1->thickness
cv2.putText(img,"OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
cv2.imshow("Image",img)

cv2.waitKey(0)