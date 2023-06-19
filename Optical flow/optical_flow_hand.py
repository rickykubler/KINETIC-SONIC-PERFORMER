import cv2
import mediapipe as mp
import numpy as np
import argparse
from pythonosc import udp_client
import math
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
mp_pose = mp.solutions.pose

"""
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
"""

# For webcam input:
cap = cv2.VideoCapture(0)

# suc = a boolean return value from getting the frame
# prev = the first frame in the entire video sequence
success, prev = cap.read()

# Converts frame to grayscale because we only need the luminance channel for
# detecting edges - less computationally expensive
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

step=16

with mp_holistic.Holistic(model_complexity=1 ,min_detection_confidence=0.0, min_tracking_confidence=0.0) as holistic:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue
  
    h, w = image.shape[:2]  ## 480,640
    y, x = (np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int))   #unità di misura/scala
    y_norm=y/480
    x_norm=x/640
    
            
    # distanza tra punto e punti
    # media pesata in base a distanza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    
    
    # To improve performance, optionally mark the image as not writeable to pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = holistic.process(image)
    
    # RIGHT WRIST
    right_wrist_x= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x
    right_wrist_y= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y
    # print(right_wrist_x)   RANGE 0.0350
    
    min_distance_squared=min(np.square(np.subtract(x_norm,right_wrist_x*np.ones_like(x_norm)))+np.square(np.subtract(y_norm,right_wrist_y*np.ones_like(y_norm))))
    index_min=np.argmin(min_distance_squared)
    print(magnitude[index_min,0]/0.06)
    
    #weighted_mag_hand=np.average(magnitude,weights = distances)
    #print(weighted_mag_hand)
    
    #Remove Nose
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].visibility = 0.0
    #Remove Left Eye
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EYE].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EYE_INNER].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EYE_OUTER].visibility = 0.0
    #Remove Right Eye
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_EYE].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_EYE_INNER].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_EYE_OUTER].visibility = 0.0
    #Remove Ears
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EAR].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_EAR].visibility = 0.0
    #Remove Mouth
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.MOUTH_RIGHT].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.MOUTH_LEFT].visibility = 0.0
    
    #Remove Left Hand
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_PINKY].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_INDEX].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_THUMB].visibility = 0.0
    #Remove Right Hand
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_PINKY].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_INDEX].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_THUMB].visibility = 0.0
    
    
    # Draw landmark annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  
    mp_drawing.draw_landmarks(
      image,
      results.right_hand_landmarks,
      mp_holistic.HAND_CONNECTIONS,
      #mp_drawing_styles.get_default_hand_landmarks_style(),
      #mp_drawing_styles.get_default_hand_connections_style()
    )

     # Updates previous frame
    prevgray = gray

    # show in two different windows the flow grid and the HSV flow
    # cv2.imshow('flow', draw_flow(gray, flow))
    # cv2.imshow('flow HSV', draw_hsv(flow))
    
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Holistic', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
  
# free up memory
cap.release()
#cv2.destroyAllWindows()

#client.send_message("on_off", 0)
#client_2.send_message("on_off", 0)