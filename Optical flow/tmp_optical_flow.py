import numpy as np
import cv2
import time

# from "OReilly Programming Computer Vision with Python" book
# PRESS q TO END THE SCRIPT
# TO CALCULATE HOW MUCH MOTION THERE IS IN THE FRAME

# manca: magnitude e direzione

# optical flow grid/field
def draw_flow(img, flow, step=16):

    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T

    lines = np.vstack([x, y, x-fx, y-fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)

    img_bgr = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.polylines(img_bgr, lines, 0, (0, 255, 0))

    for (x1, y1), (_x2, _y2) in lines:
        cv2.circle(img_bgr, (x1, y1), 1, (0, 255, 0), -1)

    return img_bgr

# optical flow HSV (colored)
def draw_hsv(flow):

    h, w = flow.shape[:2]
    fx, fy = flow[:,:,0], flow[:,:,1]

    ang = np.arctan2(fy, fx) + np.pi
    v = np.sqrt(fx*fx+fy*fy)

    hsv = np.zeros((h, w, 3), np.uint8) # Creates an image filled with zero intensities with the same dimensions as the frame (hxwx3 dimension)
    hsv[...,0] = ang*(180/np.pi/2)  # Sets image color according to the optical flow direction
    hsv[...,1] = 255  # Sets image saturation to maximum
    hsv[...,2] = np.minimum(v*4, 255)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    return bgr


# The video feed is read in as a VideoCapture object
cap = cv2.VideoCapture(0)

# suc = a boolean return value from getting the frame
# prev = the first frame in the entire video sequence
suc, prev = cap.read()

# Converts frame to grayscale because we only need the luminance channel for
# detecting edges - less computationally expensive
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)


while True:

    # suc = a boolean return value from gettingthe frame 
    # img = the current frame being projected in the video
    suc, img = cap.read()
    
    # Converts each frame to grayscale - we previously only converted the first frame to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calculates dense optical flow by Farneback method
    # https://docs.opencv.org/3.4/dc/d6b/group__video__track.html#ga5d10ebbd59fe09c5f650289ec0ece5af 
    flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    angle=angle * 180 / np.pi / 2   #vedi se normalizzazione corretta
    """
    #MEAN NORMALIZED ANGLE, WEIGHTED WITH MAGNITUDE  (RIVEDI CONCETTO)
    norm_ang=(np.average(angle,weights = magnitude))/180 
    if norm_ang<1:
        print(norm_ang)  
    else:
        norm_ang=1
        print(norm_ang)
    """
    
    #MEAN NORMALIZED MAGNITUDE, WEIGHTED WITH ANGLE
    norm_mag=np.average(magnitude,weights = angle)/10
    if norm_mag<1:
        print(norm_mag)  
    else:
        norm_mag=1
        print(norm_mag)
    
    
    # Updates previous frame
    prevgray = gray

    # show in two different windows the flow grid and the HSV flow
    cv2.imshow('flow', draw_flow(gray, flow))
    cv2.imshow('flow HSV', draw_hsv(flow))

    key = cv2.waitKey(5)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()