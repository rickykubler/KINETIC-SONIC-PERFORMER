import cv2
import mediapipe as mp
import numpy as np
import argparse
from pythonosc import udp_client
import math
import time

# PRESS q TO END THE SCRIPT

# OPTICAL FLOW TO CALCULATE HOW MUCH MOTION THERE IS IN THE FRAME

# NB: OPTICAL FLOW + VELOCITY OF POINTS SLOW DOWN THE PROCESS

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

# optical flow movement HSV (colored)
def draw_hsv(flow):

    h, w = flow.shape[:2]
    fx, fy = flow[:,:,0], flow[:,:,1]

    ang = np.arctan2(fy, fx) + np.pi
    v = np.sqrt(fx*fx+fy*fy)

    hsv = np.zeros((h, w, 3), np.uint8) # Creates an image filled with zero intensities with the same dimensions as the frame (hxwx3 dimension)
    hsv[...,0] = ang*(180/np.pi/2)      # Sets image color according to the optical flow direction
    hsv[...,1] = 255                    # Sets image saturation to maximum
    hsv[...,2] = np.minimum(v*4, 255)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    return bgr

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
mp_pose = mp.solutions.pose

# For webcam input:
cap = cv2.VideoCapture(0)

# success = a boolean return value from getting the frame
# prev = the first frame in the entire video sequence
success, prev = cap.read()

# Converts frame to grayscale because we only need the luminance channel for
# detecting edges - less computationally expensive
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

# Setting default values for right hand and head
previous_hand_x=0.5
previous_hand_y=0.5
previous_head_x=0.5
previous_head_y=0.5

# for every frame
with mp_holistic.Holistic(model_complexity=1 ,min_detection_confidence=0.0, min_tracking_confidence=0.0) as holistic:
  while cap.isOpened():
    # success = a boolean return value from gettingthe frame 
    # image = the current frame being projected in the video
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue
    
    # start time to calculate time interval between two frames
    start = time.time()
    
    # Converts each frame to grayscale - we previously only converted the first frame to grayscale         
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculates dense optical flow by Farneback method
    # https://docs.opencv.org/3.4/dc/d6b/group__video__track.html#ga5d10ebbd59fe09c5f650289ec0ece5af 
    flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    angle=angle * 180 / np.pi / 2
    
    # MEAN NORMALIZED ANGLE, WEIGHTED WITH MAGNITUDE  --> MEAN DIRECTION OF THE WHOLE MOVEMENT IN THE SCREEN
    norm_ang=(np.average(angle,weights = magnitude))/180 
    # MEAN NORMALIZED MAGNITUDE, WEIGHTED WITH ANGLE  --> MEAN VELOCITY OF THE WHOLE MOVEMENT IN THE SCREEN
    norm_mag=np.average(magnitude,weights = angle)/10
    
    # CLIPPING ANGLE AND VELOCITY
    if norm_ang>1:
      norm_ang=1 
    if norm_mag>1:
      norm_mag=1
        
    
    # To improve performance, optionally mark the image as not writeable to pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = holistic.process(image)
    
    # RIGHT WRIST
    right_wrist_x= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x
    right_wrist_y= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y
    
    # CENTER HEAD
    center_head_x= results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x
    center_head_y= results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y

    
    frame_distance_hand=((((right_wrist_x-previous_hand_x)**2 + (right_wrist_y-previous_hand_y)**2)**0.5))
    frame_distance_head=((((center_head_x-previous_head_x)**2 + (center_head_y-previous_head_y)**2)**0.5))
     # Updates head previous frame
    previous_head_x= center_head_x
    previous_head_y= center_head_y
     # Updates hand previous frame
    previous_hand_x= right_wrist_x
    previous_hand_y= right_wrist_y
    prevgray = gray
    
     # End time
    end = time.time()
    frame_time=end-start
    
    # CLIPPING HAND SPEED
    velocity_norm_hand=(frame_distance_hand/frame_time)/2
    if velocity_norm_hand>1:
        velocity_norm_hand=1
    
    # CLIPPING HEAD SPEED   
    velocity_norm_head=(frame_distance_head/frame_time)/2
    if velocity_norm_head>1:
        velocity_norm_head=1
        
    print("Head velocity:", velocity_norm_head,"Hand velocity:", velocity_norm_hand,"Mean body direction:",norm_ang, "Mean movement magnitude:",norm_mag)
    
    # calculate the FPS for current frame detection
    # fps = 1 / (end-start)
    # print(f"{fps:.2f} FPS")
    
    # Flip the image horizontally for a selfie-view display.
    # cv2.imshow('MediaPipe Holistic', cv2.flip(image, 1))
    # cv2.imshow('flow', draw_flow(gray, flow))
    cv2.imshow('flow HSV', draw_hsv(flow))
    key = cv2.waitKey(5)
    if key == ord('q'):
        break
  
# free up memory
cap.release()
cv2.destroyAllWindows()

#client.send_message("on_off", 0)
#client_2.send_message("on_off", 0)