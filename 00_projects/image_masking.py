import cv2
import numpy as np

cap = cv2.VideoCapture(0) # Initialize the webcam capture

def nothing(x): #To ensure the correct operation of the cv2.createTrackbar function, I created an empty function.
    pass


# Create a window for the Trackbar controls and set its size
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 500,500)


# Create trackbars for lower and upper HSV values
cv2.createTrackbar("Lower - H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Lower - S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Lower - V", "Trackbar", 0, 255, nothing)

cv2.createTrackbar("Upper - H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Upper - S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper - V", "Trackbar", 0, 255, nothing)

"""In OpenCV, Hue has values from 0 to 180, Saturation and Value from 0 to 255. 
Thus, OpenCV uses HSV ranges between (0-180, 0-255, 0-255)."""

# Default starting values for uppers are zeros. Initialize upper HSV trackbar values to their maximum
cv2.setTrackbarPos("Upper - H", "Trackbar", 180)
cv2.setTrackbarPos("Upper - S", "Trackbar", 255)
cv2.setTrackbarPos("Upper - V", "Trackbar", 255)


# Loop to continuously capture frames from the webcam
while True:
    
    # Read a frame from the webcam and flip it horizontally
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    # Convert the frame to BGR to HSV color space
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   

    # Get lower and upper HSV values from the trackbars
    lower_h = cv2.getTrackbarPos("Lower - H", "Trackbar")
    lower_s = cv2.getTrackbarPos("Lower - S", "Trackbar")
    lower_v = cv2.getTrackbarPos("Lower - V", "Trackbar")

    upper_h = cv2.getTrackbarPos("Upper - H", "Trackbar")
    upper_s = cv2.getTrackbarPos("Upper - S", "Trackbar")
    upper_v = cv2.getTrackbarPos("Upper - V", "Trackbar")

    # Create an array called lower_color containing the lower bounds of Hue, Saturation, and Value.
    lower_color = np.array([lower_h, lower_s, lower_v])
    
    # Create an array called upper_color containing the upper bounds of Hue, Saturation, and Value.
    upper_color = np.array([upper_h, upper_s, upper_v])


    # Use the cv2.inRange function to create a mask based on the HSV-converted image frame_hsv using these lower and upper bounds. 
    mask = cv2.inRange(frame_hsv, lower_color, upper_color)

    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

