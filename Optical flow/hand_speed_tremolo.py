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

# For webcam input:
cap = cv2.VideoCapture(0)

# suc = a boolean return value from getting the frame
# prev = the first frame in the entire video sequence
success, prev = cap.read()

# Converts frame to grayscale because we only need the luminance channel for
# detecting edges - less computationally expensive
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
previous_x=0.5
previous_y=0.5

with mp_holistic.Holistic(model_complexity=1 ,min_detection_confidence=0.0, min_tracking_confidence=0.0) as holistic:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue
    
    # start time to calculate FPS
    start = time.time()
             
    # distanza tra punto e punti
    # media pesata in base a distanza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # To improve performance, optionally mark the image as not writeable to pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = holistic.process(image)
    
    # RIGHT WRIST
    right_wrist_x= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x
    right_wrist_y= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y
    
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

    
    frame_distance=((((right_wrist_x-previous_x)**2 + (right_wrist_y-previous_y)**2)**0.5))
     # Updates previous frame
    previous_x= right_wrist_x
    previous_y= right_wrist_y
    prevgray = gray
    
     # End time
    end = time.time()
    frame_time=end-start
    velocity_norm=(frame_distance/frame_time)/2
    if velocity_norm<1:
        print(velocity_norm)  
    else:
        velocity_norm=1
        print(velocity_norm)
        
    # calculate the FPS for current frame detection
    # fps = 1 / (end-start)
    # print(f"{fps:.2f} FPS")
    
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Holistic', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
  
# free up memory
cap.release()
#cv2.destroyAllWindows()

#client.send_message("on_off", 0)
#client_2.send_message("on_off", 0)