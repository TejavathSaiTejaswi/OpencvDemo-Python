### CHAPTER 1
#### READ: IMAGES - VIDEOS - WEBCAM

In this chapter, we see how to read images, videos and webcam.
1. Import the libraries

   ````
   import numpy as np
   import cv2
   ````
   *cv2 stands for computer vision*

2. To read image using cv2, we use function called `imread`

   For example `image = cv2.imread(IMAGE_PATH)`
3. To show the output of the above read image, we use function called `imshow`. 

    For example `cv2.imshow("Output:",image)`
4. To add a delay so that we can see the image, we use a function called `waitKey()`
   - For example: `cv2.waitKey(0)` *0 to wait for infinity*
     The number indicates any value in milliseconds.
     - For example: `cv2.waitKey(1000)` *here 1000 is for 1 sec*
5. To create a video capture object, we use `cv2.VideoCapture` function

   
       cap = cv2.VideoCapture("Resources/MOVIE.mp4")
    
        while True:
            success, img = cap.read()
            cv2.imshow("Video",img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

6. Reading webcam is same as capturing video. The only thing that changes is giving an id instead of path
We can set the parameters of the webcam by setting the id's.
*id 3 is width,id 4 is height, id 10 for brightness etc...*
    
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

### CHAPTER 2
#### BASIC FUNCTIONS

In this chapter, we look at the basic functions required while building opencv projects
`cv2.cvtColor` converts your image into different color spaces.
In general, we use RGB convention.But in opencv we use `BGR` convention.

1. To convert into a grey scale image, we use `cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)`

2. Inorder to add Gaussian blur function to blur our image, we use

    `imgBlur = cv2.GaussianBlur(image,(7,7),0)`

    where,
    
        image is the image you want to add the blur function,
        the kernel size in (7,7),
        and sigmax is 0
3. To find edges in our image, we use Canny edge detector

         imgCanny = cv2.Canny(img,100,100)
         where
         100 is threshold

4. Similarly, to decrease the number of edge detectors, we increase the threshold

       imgCanny = cv2.Canny(img,150,200)

5. To increase the thickness of the edge detector, we use `cv2.dilate`

       kernel = np.ones((5,5),np.uint8)
       imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
       #imgDialation = cv2.dilate(imgCanny,kernel.iterations=5)

6. To make te edge detector thinner, we use `cv2.erode`

       imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

### CHAPTER 3
#### RESIZING AND CROPPING

In mathematics the +x axis is towards the east, +y axis is towards the north
But in opencv the +x axis is towards the east(same), +y axis is towards the south.
1. To resize the image, we use `cv2.resize`

       # 300 is width, 200 is height
       imgResize = cv2.resize(img,(300,200))
It can't increase the quality, it can increase the pixel size

2. Next is cropping the image. Cropping can be very useful in getting the information from specific parts of the image. 
Image is just a matrix or an array of pixels. 
Here we are not using opencv function instead matrix functionality itself.

**Note:** In the above opencv function, it is width and height whereas in matrix it is height and width

       imgCropped = img[0:200,200:500]

### CHAPTER 4
#### SHAPES AND TEXTS

1. To create a matrix filled with zeros. Here zeros means filled with black

       img_greyscale = np.zeros((512,512)) is a greyscale image
       #color functionality, add 3
       img = np.zeros((512,512,3),np.uint8)

       #to color the whole image
       img[:] = 255,0,0

2. To create lines we have `cv2.line` function whereas to create a rectangle and circle, we have `cv2.rectangle` and `cv2.circle` respectively
To fill the rectangle or circle, we can use `cv2.FILLED` argument
        
       #parameters are start point, end point, color, and thickness
       # cv2.line(img,(0,0),(300,300),(0,255,0),3)
       #img.shape[1]-> width;img.shape[0]-> height
       cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
       cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
       #to fill the rectangle
       # cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
       cv2.circle(img,(400,50),30,(255,255,0),5)
3. To put text, we can use `cv2.putText` with desired arguments

       #img-> image;"OPENCV "->text;(300,200)->origin;cv2.FONT_HERSHEY_COMPLEX->font;1->scale;(0,150,0)->color;1->thickness
       cv2.putText(img,"OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
       cv2.imshow("Image",img)

### CHAPTER 5
#### WARP PERSPECTIVE

1. To get the perspective transform, we can use `cv2.getPerspectiveTransform` function and to get the warp perspective we can use `cv2.warpPerspective` function


       # img = cv2.imread("Resources/cards.jpg")
       img = cv2.imread("Resources/Screenshot.png")
       width,height = 250,350
       pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
       pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
       matrix = cv2.getPerspectiveTransform(pts1,pts2)
       imgOutput = cv2.warpPerspective(img,matrix,(width,height))
       cv2.imshow("Input",img)
       cv2.imshow("Output Image",imgOutput)

### CHAPTER 6
#### JOINING IMAGES

1. To stack images horizontally as well as vertically, we use numpy functions instead of opencv functions

       #numpy functions(not opencv function)
       imgHor = np.hstack((img,img))
       imgVer = np.vstack((img,img))
       #The issues with this is we cannot resize the image. It can take whole space.
       #the other one is all the images should be of the same number of channels as we are talking about the matrices
**Note: ** The issues with using this function is we cannot resize the image. It can take whole space.
The other one is all the images should be of the same number of channels as we are talking about the matrices

2. The function to solve the above problem is .......(TODO)


### CHAPTER 7
#### COLOR DETECTION

1. To get a Window with a name, we use `cv2.namedWindow` function. Here we create a window `TrackBars` to get Hue, Saturation and Value.
   
       cv2.namedWindow("TrackBars")
2. To get the resized window, we use `cv2.resizeWindow` function

       cv2.resizeWindow("TrackBars",640,240)
3. We create 6 different trackbars to create the hue, saturation and value 

       #Hue min is 0 max can be 179 in opencv
       # cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
       # cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
       # cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
       # cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
       # cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
       # cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

You can get the original wanted color by masking the required part in white and the other things should be in black

4. To convert the image into a hsv image
    
       imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
5. Get Hue,saturation and value from the trackbar position using `cv2.getTrackbarPos` function

       h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
       h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
       s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
       s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
       v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
       v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
6. Get the upper and lower range of Hue,saturation and value    
       
       lower = np.array([h_min,s_min,v_min])
       upper = np.array([h_max, s_max, v_max])
7. Mask the HSV image if the value lies between the upper and lower boundary using `cv2.inRange` function
       
       mask = cv2.inRange(imgHSV,lower,upper)
8. To covert the mask from black and white to color, we use `cv2.bitwise_and` function  
       
       imgResult = cv2.bitwise_and(img,img,mask=mask)

### CHAPTER 8
#### CONTOURS/SHAPE DETECTION
