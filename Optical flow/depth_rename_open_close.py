import cv2
import mediapipe as mp
import numpy as np
import argparse
from pythonosc import udp_client
import math
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
mp_pose = mp.solutions.pose

# For webcam input:
cap = cv2.VideoCapture(0)

with mp_holistic.Holistic(model_complexity=1 ,min_detection_confidence=0.0, min_tracking_confidence=0.0) as holistic:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue
  
    # To improve performance, optionally mark the image as not writeable to pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = holistic.process(image)
    
    
    # right hand (points 16,18,20)
    right_wrist_x= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x
    right_wrist_y= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y
    right_pinky_x= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_PINKY].x
    right_pinky_y= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_PINKY].y
    right_index_x= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].x
    right_index_y= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].y
    
    center_right_hand_x= (right_wrist_x+right_pinky_x+right_index_x)/3
    center_right_hand_y= (right_wrist_y+right_pinky_y+right_index_y)/3  ## calculate momentum (???) of this point
    # print (center_right_hand_x, center_right_hand_y)
    right_wrist_x= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].z
    # print(right_wrist_x)
    
  
    
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
    
    #open/close
    if results.right_hand_landmarks:
      thumb_x=results.right_hand_landmarks.landmark[4].x
      thumb_y=results.right_hand_landmarks.landmark[4].y
      index_x=results.right_hand_landmarks.landmark[8].x
      index_y=results.right_hand_landmarks.landmark[8].y
      middle_x=results.right_hand_landmarks.landmark[12].x
      middle_y=results.right_hand_landmarks.landmark[12].y
      ring_x=results.right_hand_landmarks.landmark[16].x
      ring_y= results.right_hand_landmarks.landmark[16].y
      pinky_x=results.right_hand_landmarks.landmark[20].x
      pinky_y=results.right_hand_landmarks.landmark[20].y
      wrist_x=results.right_hand_landmarks.landmark[0].x
      wrist_y=results.right_hand_landmarks.landmark[0].y
    
    center_x=(thumb_x+index_x+middle_x+ring_x+pinky_x)/5
    center_y=(thumb_y+index_y+middle_y+ring_y+pinky_y)/5
    
    distance_thumb=((center_x - thumb_x)**2 + (center_y - thumb_y)**2)**0.5
    distance_index=((center_x - index_x)**2 + (center_y - index_y)**2)**0.5
    distance_middle=((center_x - middle_x)**2 + (center_y - middle_y)**2)**0.5
    distance_ring=((center_x - ring_x)**2 + (center_y - ring_y)**2)**0.5
    distance_pinky=((center_x - pinky_x)**2 + (center_y - pinky_y)**2)**0.5
    
    distance_tot= distance_thumb + distance_index + distance_middle + distance_ring +  distance_pinky
    
    treshold=0.4
    
    """
    if distance_tot<treshold:
      print("CLOSED")
    else:
      print("OPEN")
    """
    #rotation
    coord_x_right = middle_x - wrist_x
    coord_y_right = middle_y - wrist_y

    right_hand_angle = abs(math.atan2(coord_x_right, coord_y_right))/math.pi
    print(right_hand_angle)

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
    
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Holistic', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
# free up memory
cap.release()
#cv2.destroyAllWindows()

#client.send_message("on_off", 0)
#client_2.send_message("on_off", 0)