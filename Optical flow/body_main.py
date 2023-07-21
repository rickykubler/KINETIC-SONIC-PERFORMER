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

# PRESS q TO END THE SCRIPT

# OPTICAL FLOW TO CALCULATE HOW MUCH MOTION THERE IS IN THE FRAME
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
#OSC client setting
def setOSC_Client(IP_address, nPort):
  # argparse helps writing user-friendly commandline interfaces
  Parser = argparse.ArgumentParser()
  Parser.add_argument("--ip", default=IP_address, help="The ip of the OSC server")
  Parser.add_argument("--port", type=int, default=nPort)
  # Parse the arguments
  args, unknown = Parser.parse_known_args()
  # Start the UDP Client
  client = udp_client.SimpleUDPClient(args.ip, args.port)
   
  return client

# For webcam input:
cap = cv2.VideoCapture(0)

# start the osc
START_SOUND = True

Max8_IP='192.168.1.213'
Max8_IP_port=7400

MusicVAE_IP='192.168.1.159'
MusicVAE_port=7400

#Connect with Max8 on other laptop
client_Max8 = setOSC_Client(Max8_IP, Max8_IP_port)
#Connect with MusicVAE on other laptop
client_MusicVAE = setOSC_Client(MusicVAE_IP, MusicVAE_port)

# success = a boolean return value from getting the frame, prev = the first frame in the entire video sequence
success, prev = cap.read()

# Converts frame to grayscale because we only need the luminance channel for detecting edges - less computationally expensive
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

# Setting default values for right hand and head
previous_right_hand_x=0.1
previous_right_hand_y=0.1

#previous_right_hand_x=0.5
#previous_right_hand_y=0.5
previous_head_x=0.5
previous_head_y=0.5
previous_left_hand_x=0.5
previous_left_hand_y=0.5

previous_right_hand_v = 0.0
previous_left_hand_v = 0.0
previous_head_v = 0.0

# for every frame
with mp_holistic.Holistic(model_complexity=1 ,min_detection_confidence=0.0, min_tracking_confidence=0.0) as holistic:
  while cap.isOpened():
    # success = a boolean return value from gettingthe frame , image = the current frame being projected in the video
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue
  
    # To improve performance, optionally mark the image as not writeable to pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imageBackup = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = holistic.process(image)
    
    # start time to calculate time interval between two frames
    start = time.time()
    
    # Converts each frame to grayscale - we previously only converted the first frame to grayscale         
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculates dense optical flow by Farneback method
    flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    angle=angle * 180 / np.pi / 2
    
    # 1) MEAN NORMALIZED ANGLE, WEIGHTED WITH MAGNITUDE  --> MEAN DIRECTION OF THE WHOLE MOVEMENT IN THE SCREEN
    # tende a 1 verso l'alto, a 0 verso il basso, 0,5 a dx e sx, la distanza influisce perchè più sei vicino più punti sullo schermo sono presi
    # se fermo o fuori dallo schermo il valore è 0
    norm_ang=(np.average(angle,weights = magnitude))/180 
    # 2) MEAN NORMALIZED MAGNITUDE, WEIGHTED WITH ANGLE  --> MEAN VELOCITY OF THE WHOLE MOVEMENT IN THE SCREEN
    # se fermo o fuori dallo schermo il valore è 0
    norm_mag=np.average(magnitude,weights = angle)/10
    
    # CLIPPING ANGLE AND VELOCITY
    if norm_ang>1:
      norm_ang=1 
    if norm_mag>1:
      norm_mag=1

    # 3) DEPTH THE HEAD AND OF THE RIGHT WRIST (used also to adapt parameters wrt the distance from camera)
    head_depth= results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].z
    right_wrist_depth= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].z
    
    # IMPORTANT: RESIZE PARAMETER WRT DISTANCE (DEPTH NORMALIZATION)
    # "head_depth" is pretty linear --> variation of 1 means variation of 0,6 meters in depth, variation of 2 means variation of 1,20 meters
    #  in this way *0.6 converts the number in meters, do not touch
    # /2 (2 maximum distance perceived) gives a normalization of distance, a percentage of how much you are distant
    resize=((3-abs(head_depth))*(0.6))/2
    # /1.7 (1.7 maximum distance perceived) gives a normalization of distance, a percentage of how much you are distant
    resize_hand=((3-abs(right_wrist_depth))*(0.6))/(1.7)
    
    # 4) OPEN/CLOSE RIGHT HAND & LEFT HAND WITH DISTANCE OF FINGERS'TIPS FROM PALM CENTER
    if not results.right_hand_landmarks:
      right_thumb_x=0
      right_thumb_y=0
   
      right_index_x=0
      right_index_y=0
    
      right_middle_x=0
      right_middle_y=0
    
      right_ring_x=0
      right_ring_y=0
  
      right_pinky_x=0
      right_pinky_y=0
    
      Rwrist_x=0
      Rwrist_y=0
    
    if results.right_hand_landmarks:
      right_thumb_x=results.right_hand_landmarks.landmark[4].x
      right_thumb_y=results.right_hand_landmarks.landmark[4].y
   
      right_index_x=results.right_hand_landmarks.landmark[8].x
      right_index_y=results.right_hand_landmarks.landmark[8].y
    
      right_middle_x=results.right_hand_landmarks.landmark[12].x
      right_middle_y=results.right_hand_landmarks.landmark[12].y
    
      right_ring_x=results.right_hand_landmarks.landmark[16].x
      right_ring_y=results.right_hand_landmarks.landmark[16].y
  
      right_pinky_x=results.right_hand_landmarks.landmark[20].x
      right_pinky_y=results.right_hand_landmarks.landmark[20].y
    
      Rwrist_x=results.right_hand_landmarks.landmark[0].x
      Rwrist_y=results.right_hand_landmarks.landmark[0].y

    if not results.right_hand_landmarks:
      left_thumb_x=0
      left_thumb_y=0
   
      left_index_x=0
      left_index_y=0
    
      left_middle_x=0
      left_middle_y=0
    
      left_ring_x=0
      left_ring_y=0
  
      left_pinky_x=0
      left_pinky_y=0
    
      Lwrist_x=0
      Lwrist_y=0
    
    if results.left_hand_landmarks:
      left_thumb_x=results.left_hand_landmarks.landmark[4].x
      left_thumb_y=results.left_hand_landmarks.landmark[4].y
   
      left_index_x=results.left_hand_landmarks.landmark[8].x
      left_index_y=results.left_hand_landmarks.landmark[8].y
    
      left_middle_x=results.left_hand_landmarks.landmark[12].x
      left_middle_y=results.left_hand_landmarks.landmark[12].y
    
      left_ring_x=results.left_hand_landmarks.landmark[16].x
      left_ring_y=results.left_hand_landmarks.landmark[16].y
  
      left_pinky_x=results.left_hand_landmarks.landmark[20].x
      left_pinky_y=results.left_hand_landmarks.landmark[20].y
    
      Lwrist_x=results.left_hand_landmarks.landmark[0].x
      Lwrist_y=results.left_hand_landmarks.landmark[0].y
      
    # CENTER RIGHT HAND & LEFT HAND
    right_hand_center_x=(right_thumb_x+right_index_x+right_middle_x+right_ring_x+right_pinky_x)/5
    right_hand_center_y=(right_thumb_x+right_index_y+right_middle_y+right_ring_y+right_pinky_y)/5
    left_hand_center_x=(left_thumb_x+left_index_x+left_middle_x+left_ring_x+left_pinky_x)/5
    left_hand_center_y=(left_thumb_x+left_index_y+left_middle_y+left_ring_y+left_pinky_y)/5
    
    # DISTANCE BETWEEN EVERY FINGER AND CENTER OF THE RIGHT PALM & LEFT PALM
    right_hand_distance_thumb=((right_hand_center_x - right_thumb_x)**2 + (right_hand_center_y - right_thumb_y)**2)**0.5
    #right_hand_distance_index=((right_hand_center_x - right_index_x)**2 + (right_hand_center_y - right_index_y)**2)**0.5  SE TI ALLONTANI MEDIAPIPE DA' PROBLEMI SOPRATTUTTO CON INDICE
    right_hand_distance_middle=((right_hand_center_x - right_middle_x)**2 + (right_hand_center_y - right_middle_y)**2)**0.5
    right_hand_distance_ring=((right_hand_center_x - right_ring_x)**2 + (right_hand_center_y - right_ring_y)**2)**0.5
    right_hand_distance_pinky=((right_hand_center_x - right_pinky_x)**2 + (right_hand_center_y - right_pinky_y)**2)**0.5
    
    left_hand_distance_thumb=((left_hand_center_x - left_thumb_x)**2 + (left_hand_center_y - left_thumb_y)**2)**0.5
    #left_hand_distance_index=((left_hand_center_x - left_index_x)**2 + (left_hand_center_y - left_index_y)**2)**0.5  SE TI ALLONTANI MEDIAPIPE DA' PROBLEMI SOPRATTUTTO CON INDICE
    left_hand_distance_middle=((left_hand_center_x - left_middle_x)**2 + (left_hand_center_y - left_middle_y)**2)**0.5
    left_hand_distance_ring=((left_hand_center_x - left_ring_x)**2 + (left_hand_center_y - left_ring_y)**2)**0.5
    left_hand_distance_pinky=((left_hand_center_x - left_pinky_x)**2 + (left_hand_center_y - left_pinky_y)**2)**0.5
    
    # TOTAL DISTANCE OF FINGER TIPS FROM PALM CENTER (*resize TO ADAPT THE PARAMETER WRT DISTANCE)
    # se lontana il resize influisce poco, se vicina il resize influisce di più
    right_hand_distance_tot= (right_hand_distance_thumb + right_hand_distance_middle + right_hand_distance_ring +  right_hand_distance_pinky)*resize_hand
    left_hand_distance_tot= (left_hand_distance_thumb + left_hand_distance_middle + left_hand_distance_ring +  left_hand_distance_pinky)*resize_hand
    
    # THRESHOLD FOR OPEN/CLOSE RESIZED
    treshold=0.2*resize_hand   # si può modificare 0.2 o al massimo aggiungere indice, con 0.2 e senza indice a me dà i risultati migliori
    
    if right_hand_distance_tot<treshold:
      right_hand_open_close = 0 #hand is closed
    else:
      right_hand_open_close = 1 #hand is open

    if left_hand_distance_tot<treshold:
      left_hand_open_close = 0 #hand is closed
    else:
      left_hand_open_close = 1 #hand is open
      
    # 5) GRADUAL OPENING THE RIGHT HAND & LEFT HAND (*resize ALREADY DONE IN right_hand_distance_tot) (O.25 IS THE NORMALIZATION), per adesso dà valori - considerando la distanza - tra 0.3 e 0.85
    right_hand_distance_tot_norm= (right_hand_distance_tot)/0.5
    left_hand_distance_tot_norm= (left_hand_distance_tot)/0.5
    
    #Normalized between max value and min value.
    right_hand_distance_tot_norm = (right_hand_distance_tot_norm - 0.2)/0.4 
    left_hand_distance_tot_norm = (left_hand_distance_tot_norm - 0.2)/0.4 

    if right_hand_distance_tot_norm>1:
        right_hand_distance_tot_norm=1
    if right_hand_distance_tot_norm<0:
        right_hand_distance_tot_norm=0

    if left_hand_distance_tot_norm>1:
        left_hand_distance_tot_norm=1
    if left_hand_distance_tot_norm<0:
        left_hand_distance_tot_norm=0

    # 6) ROTATION OF THE RIGHT HAND & LEFT HAND
    coord_x_right = right_middle_x - Rwrist_x
    coord_y_right = right_middle_y - Rwrist_y
    right_hand_angle = abs(math.atan2(coord_x_right, coord_y_right))/math.pi
    
    coord_x_left = left_middle_x - Lwrist_x
    coord_y_left = left_middle_y - Lwrist_y
    left_hand_angle = abs(math.atan2(coord_x_left, coord_y_left))/math.pi
    
    # RIGHT HAND WRIST  (fare solo un wrist?)
    right_wrist_x= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x
    right_wrist_y= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y
    
    # LEFT HAND WRIST
    left_wrist_x= results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x
    left_wrist_y= results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y
    
    # CENTER HEAD
    center_head_x= 1-results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x
    center_head_y= 1-results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y
    
    # HANDS ANGULATION: HANDS HEIGHT + HANDS EXPANSION
    # 7) HANDS HEIGHT --> MIDDLE POINT BETWEEN WRISTS, FOR NOW DOES NOT DEPEND ON DISTANCE 
    hands_mean_x= (1-((left_wrist_x+right_wrist_x)/2)*resize)   
    hands_mean_y= (1-((left_wrist_y+right_wrist_y)/2)*resize)   
    if hands_mean_y>1:
        hands_mean_y=1 
    if hands_mean_x>1:
        hands_mean_x=1 
    
    # 8) HANDS EXPANSION  --> EUCLIDEAN DISTANCE BETWEEN HANDS (*resize TO ADAPT THE PARAMETER WRT DISTANCE)
    right_hand_expansion= ((((right_wrist_x-left_wrist_x)**2 + (right_wrist_x-left_wrist_y)**2)**0.5))*resize
    # right_hand_expansion= (((center_right_hand_x-center_left_hand_x)**2 + (center_right_hand_y-center_left_hand_y)**2)**0.5)/abs(center_head)
    if right_hand_expansion>1:
        right_hand_expansion=0.5

    left_hand_expansion= ((((left_wrist_x-right_wrist_x)**2 + (left_wrist_x-right_wrist_y)**2)**0.5))*resize
    # left_hand_expansion= (((center_right_hand_x-center_left_hand_x)**2 + (center_right_hand_y-center_left_hand_y)**2)**0.5)/abs(center_head)
    if left_hand_expansion>1:
        left_hand_expansion=0.5
        
    # TO CALCULATE HEAD AND HAND SPEED
    #frame_distance_right_hand=((((right_wrist_x-previous_right_hand_x)**2 + (right_wrist_y-previous_right_hand_y)**2)**0.5))
    frame_distance_right_hand=((((right_middle_x-previous_right_hand_x)**2 + (right_middle_y-previous_right_hand_y)**2)**0.5))
    
    frame_distance_left_hand=((((left_wrist_x-previous_left_hand_x)**2 + (left_wrist_y-previous_left_hand_y)**2)**0.5))
    frame_distance_head=((((center_head_x-previous_head_x)**2 + (center_head_y-previous_head_y)**2)**0.5))
    
     # Updates head previous frame
    previous_head_x= center_head_x
    previous_head_y= center_head_y
     # Updates hand previous frame
    #previous_right_hand_x= right_wrist_x
    #previous_right_hand_y= right_wrist_y
    previous_right_hand_x= right_middle_x
    previous_right_hand_y= right_middle_y
    
    prevgray = gray
    
     # End time
    end = time.time()
    frame_time=end-start
    
    # 9) CLIPPING RIGHT HAND SPEED & ACCELERATION
    #velocity_norm_right_hand=((frame_distance_right_hand/frame_time)/2)   #*resize_hand???
    velocity_norm_right_hand=((frame_distance_right_hand/frame_time))   #*resize_hand???
    
    #print((frame_distance_right_hand/frame_time))
    #print(velocity_norm_right_hand)
    if velocity_norm_right_hand>1:
       velocity_norm_right_hand=1
    
    deltaV_righthand = ((velocity_norm_right_hand - previous_right_hand_v))
    previous_right_hand_v = velocity_norm_right_hand
    
    acceleration_norm_right_hand =  (deltaV_righthand/frame_time)/10
    if acceleration_norm_right_hand>1:
       acceleration_norm_right_hand=1

    # 10) CLIPPING HEAD SPEED & ACCELERATION
    velocity_norm_head=((frame_distance_head/frame_time)/2)    #*resize???
    if velocity_norm_head>1:
        velocity_norm_head=1
    
    deltaV_head = ((velocity_norm_head - previous_head_v))
    previous_head_v = velocity_norm_head
    
    acceleration_head =  (deltaV_head/frame_time)/10
    if acceleration_head>1:
       acceleration_head=1

    # 11) CLIPPING LEFT HAND SPEED & ACCELERATION
    velocity_norm_left_hand=((frame_distance_left_hand/frame_time)/2)    #*resize???
    if velocity_norm_left_hand>1:
        velocity_norm_left_hand=1

    deltaV_lefthand = ((velocity_norm_left_hand - previous_left_hand_v))
    previous_left_hand_v = velocity_norm_left_hand
    
    acceleration_norm_left_hand = (deltaV_lefthand/frame_time)/10
    if acceleration_norm_left_hand>1:
       acceleration_norm_left_hand=1
    
        
    # VARIOUS PRINTS 
    #print(f"\rRight hand's speed: {velocity_norm_right_hand} ")
    #print(f"\rRight hand's acceleration: {acceleration_norm_right_hand} ")
    #print(f"\rLeft hand's acceleration: {acceleration_norm_left_hand} ")
    #print(f"\rHead's acceleration: {acceleration_head} ")
    #print(f"\rHead's speed: {velocity_norm_head} ", end='', flush=True)
    #print(f"\rRight hand is open/close: {right_hand_open_close} ", end='', flush=True)
    #print(f"\rHands' expansion: {right_hand_expansion} ")
    #print(f"\rAverage hands' height: {hands_mean_y} ")
    # print(f"\rRight hand's rotation: {right_hand_angle} ", end='', flush=True)
    #print(f"\rRight hand's gradual opening: {right_hand_distance_tot_norm}")
    #print(f"\rDistance from camera: {resize} ")
    #print(f"\rDistance of right hand from camera: {resize_hand} ")
    #print(f"\rMean direction of body's movement: {norm_ang} ", end='', flush=True)
    #print(f"\rMean magnitude of body's movement:: { norm_mag} ", end='', flush=True)
    
    # 12) Remove elements from UI

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
    
    #Remove Left Hand Wrist
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_PINKY].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_INDEX].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_THUMB].visibility = 0.0
    #Remove Right Hand Wrist
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_PINKY].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_INDEX].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_THUMB].visibility = 0.0
    
    #Remove Left Leg&Foot
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_KNEE].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_ANKLE].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_HEEL].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_FOOT_INDEX].visibility = 0.0
    #Remove Right Leg&Foot
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_KNEE].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_ANKLE].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_HEEL].visibility = 0.0
    results.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_FOOT_INDEX].visibility = 0.0
    
    if START_SOUND:  
            #MESSAGES TO MAX8
            client_Max8.send_message("/body/hands/heightAVG",hands_mean_y)
            #client_Max8.send_message("/body/hands/xaxisAVG",hands_mean_x)
            #Right Hand 
            client_Max8.send_message("/body/righthand/openClose", right_hand_open_close)
            client_Max8.send_message("/body/righthand/speed", velocity_norm_right_hand)
            client_Max8.send_message("/body/righthand/acceleration", acceleration_norm_right_hand)
            client_Max8.send_message("/body/righthand/expansion", right_hand_expansion)
            client_Max8.send_message("/body/righthand/rotation", right_hand_angle)
            client_Max8.send_message("/body/righthand/gradualOpening", right_hand_distance_tot_norm)
            client_Max8.send_message("/body/righthand/camDistance", resize_hand)
            client_Max8.send_message("/body/righthand/x", right_wrist_x)
            client_Max8.send_message("/body/righthand/y", right_wrist_y)
            
            #Left Hand
            client_Max8.send_message("/body/lefthand/openClose", left_hand_open_close)
            client_Max8.send_message("/body/lefthand/speed", velocity_norm_left_hand)
            client_Max8.send_message("/body/lefthand/acceleration", acceleration_norm_left_hand)
            client_Max8.send_message("/body/lefthand/expansion", left_hand_expansion)
            client_Max8.send_message("/body/lefthand/rotation", left_hand_angle)
            client_Max8.send_message("/body/lefthand/gradualOpening", left_hand_distance_tot_norm)
            #client_Max8.send_message("/body/lefthand/camDistance", resize_hand)
            client_Max8.send_message("/body/lefthand/x", left_wrist_x)
            client_Max8.send_message("/body/lefthand/y", left_wrist_y)
          
            #Head
            client_Max8.send_message("/body/head/speed", velocity_norm_head)
            #client_Max8.send_message("/body/head/acceleration", acceleration_head)
            client_Max8.send_message("/body/head/camDistance", resize)
            client_Max8.send_message("/body/head/centerX", center_head_x)
            client_Max8.send_message("/body/head/centerY", center_head_y)
            
            #Body
            client_Max8.send_message("/body/body/direction", norm_ang)
            client_Max8.send_message("/body/body/velocity", norm_mag)
            
            
            #MESSAGES TO MUSIC VAE
            client_MusicVAE.send_message("/body/hands/heightAVG",hands_mean_y)
            #client_MusicVAE.send_message("/body/hands/xaxisAVG",hands_mean_x)
            
            #Right Hand 
            client_MusicVAE.send_message("/body/righthand/openClose", right_hand_open_close)
            client_MusicVAE.send_message("/body/righthand/speed", velocity_norm_right_hand)
            #client_MusicVAE.send_message("/body/righthand/acceleration", acceleration_norm_right_hand)
            client_MusicVAE.send_message("/body/righthand/expansion", right_hand_expansion)
            client_MusicVAE.send_message("/body/righthand/rotation", right_hand_angle)
            client_MusicVAE.send_message("/body/righthand/gradualOpening", right_hand_distance_tot_norm)
            client_MusicVAE.send_message("/body/righthand/camDistance", resize_hand)
            client_Max8.send_message("/body/righthand/x", right_wrist_x)
            client_Max8.send_message("/body/righthand/y", right_wrist_y)
            
            #Left Hand
            client_MusicVAE.send_message("/body/lefthand/openClose", left_hand_open_close)
            client_MusicVAE.send_message("/body/lefthand/speed", velocity_norm_left_hand)
            client_MusicVAE.send_message("/body/lefthand/acceleration", acceleration_norm_left_hand)
            client_MusicVAE.send_message("/body/lefthand/expansion", left_hand_expansion)
            client_MusicVAE.send_message("/body/lefthand/rotation", left_hand_angle)
            client_MusicVAE.send_message("/body/lefthand/gradualOpening", left_hand_distance_tot_norm)
            #client_MusicVAE.send_message("/body/lefthand/camDistance", resize_hand)
            client_Max8.send_message("/body/lefthand/x", left_wrist_x)
            client_Max8.send_message("/body/lefthand/y", left_wrist_y)
            
            #Head
            client_MusicVAE.send_message("/body/head/speed", velocity_norm_head)
            #client_MusicVAE.send_message("/body/head/acceleration", acceleration_head)
            client_MusicVAE.send_message("/body/head/camDistance", resize)
            client_MusicVAE.send_message("/body/head/centerX", center_head_x)
            client_MusicVAE.send_message("/body/head/centerY", center_head_y)
            
            #Body
            client_MusicVAE.send_message("/body/body/direction", norm_ang)
            client_MusicVAE.send_message("/body/body/velocity", norm_mag)
            
            
    # Draw landmark annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.face_landmarks,
        mp_holistic.FACEMESH_TESSELATION,
        landmark_drawing_spec=None,
        connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style()
    )
    mp_drawing.draw_landmarks(
        image,
        results.face_landmarks,
        mp_holistic.FACEMESH_CONTOURS,
        landmark_drawing_spec=None,
        #connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style()
    )
    mp_drawing.draw_landmarks(
      image,
      results.pose_landmarks,
      mp_holistic.POSE_CONNECTIONS,
      #landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style() 
    )
    mp_drawing.draw_landmarks(
      image,
      results.left_hand_landmarks,
      mp_holistic.HAND_CONNECTIONS
    )
    mp_drawing.draw_landmarks(
      image,
      results.right_hand_landmarks,
      mp_holistic.HAND_CONNECTIONS
    )
    
    
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Holistic', cv2.flip(image, 1))
    #cv2.imshow('Clean image', cv2.flip(image, 1))
    #cv2.imshow('flow', cv2.flip(draw_flow(gray, flow),1))
    #cv2.imshow('flow HSV', cv2.flip(draw_hsv(flow),1))
    key = cv2.waitKey(5)
    if key == ord('q'):
        break
  
# free up memory
cap.release()
cv2.destroyAllWindows()

client_Max8.send_message("on_off", 0)
client_MusicVAE.send_message("on_off", 0)