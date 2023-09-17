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

# OPTICAL FLOW FUNCTIONS:
# DRAW OPTICAL FLOW VECTORS
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
# DRAW OPTICAL FLOW MOVEMENT HSV (COLOURED)
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

# OSC CLIENT SETTINGS
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

# FOR WEBCAM INPUT:
cap = cv2.VideoCapture(0)

# START OSC:
START_SOUND = True

Max8_IP='192.168.1.213'
Max8_IP_port=7374

MusicVAE_IP='192.168.1.159'
MusicVAE_port=7400

# CONNECT WITH Max8 
client_Max8 = setOSC_Client(Max8_IP, Max8_IP_port)
# CONNECT WITH MusicVAE 
client_MusicVAE = setOSC_Client(MusicVAE_IP, MusicVAE_port)

# SUCCESS = A BOOLEAN RETURN VALUE FROM GETTING THE FRAME,   PREV = THE FIRST FRAME IN THE ENTIRE VIDEO SEQUENCE
success, prev = cap.read()

# CONVERTS FRAME TO GRAYSCALE BECAUSE WE ONLY NEED THE LUMINANCE CHANNEL FOR DETECTING EDGES, LESS COMPUTATIONALLY EXPENSIVE
prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

# SETTING DEFAULT VALUES FOR HANDS AND HEAD 
previous_right_hand_x=0.5
previous_right_hand_y=0.5
previous_head_x=0.5
previous_head_y=0.5
previous_left_hand_x=0.5
previous_left_hand_y=0.5

previous_right_hand_v = 0.0
previous_left_hand_v = 0.0
previous_head_v = 0.0

#BUFFER
buffer=np.zeros(10)

# FOR EVERY FRAME
with mp_holistic.Holistic(model_complexity=1 ,min_detection_confidence=0.0, min_tracking_confidence=0.0) as holistic:
  while cap.isOpened():
    # success = a boolean return value from gettingthe frame , image = the current frame being projected in the video
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue
  
    # to improve performance, optionally mark the image as not writeable to pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imageBackup = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = holistic.process(image)
    
    # start time to calculate time interval between two frames
    start = time.time()
    
    # Converts each frame to grayscale - we previously only converted the first frame to grayscale         
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # CALCULATES DENSE OPTICAL FLOW BY FARNEBACK METHOD
    flow = cv2.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    angle=angle * 180 / np.pi / 2
    
    # 1) MEAN NORMALIZED ANGLE, WEIGHTED WITH MAGNITUDE  --> MEAN DIRECTION OF THE WHOLE MOVEMENT IN THE SCREEN (tende a 1 verso l'alto, a 0 verso il basso, 0,5 a dx e sx, la distanza influisce perchè più sei vicino più punti sullo schermo sono presi se fermo o fuori dallo schermo il valore è 0)
    norm_ang=(np.average(angle,weights = magnitude))/180 
    # 2) MEAN NORMALIZED MAGNITUDE, WEIGHTED WITH ANGLE  --> MEAN VELOCITY OF THE WHOLE MOVEMENT IN THE SCREEN (se fermo o fuori dallo schermo il valore è 0)
    norm_mag=np.average(magnitude,weights = angle)/10
    
    # BUFFER
    buffer=buffer[:-1]
    buffer=np.append(norm_mag, buffer)
    print(buffer)
    
    # CLIPPING ANGLE AND VELOCITY
    if norm_ang>1:
      norm_ang=1 
    if norm_mag>1:
      norm_mag=1

    # 3) DEPTH THE HEAD AND OF THE RIGHT WRIST (used also to adapt parameters wrt the distance from camera)
    head_depth= results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].z
    right_wrist_depth= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].z
    
    # IMPORTANT: "RESIZE" PARAMETER WRT DISTANCE, DEPTH NORMALIZATION ("head_depth" is pretty linear --> variation of 1 means variation of 0,6 meters in depth, variation of 2 means variation of 1,20 meters in this way *0.6 converts the number in meters, do not touch /2 (2 maximum distance perceived) gives a normalization of distance, a percentage of how much you are distant)
    resize=((3-abs(head_depth))*(0.6))/2
    # /1.7 (1.7 maximum distance perceived) gives a normalization of distance, a percentage of how much you are distant
    resize_hand=((3-abs(right_wrist_depth))*(0.6))/(1.7)
    
    # 4) OPEN/CLOSE RIGHT HAND WITH DISTANCE OF FINGERS'TIPS FROM PALM CENTER
    if not results.right_hand_landmarks:
      thumb_x=0
      thumb_y=0
   
      index_x=0
      index_y=0
    
      middle_x=0
      middle_y=0
    
      ring_x=0
      ring_y=0
  
      pinky_x=0
      pinky_y=0
    
      wrist_x=0
      wrist_y=0
    
    if results.right_hand_landmarks:
      thumb_x=results.right_hand_landmarks.landmark[4].x
      thumb_y=results.right_hand_landmarks.landmark[4].y
   
      index_x=results.right_hand_landmarks.landmark[8].x
      index_y=results.right_hand_landmarks.landmark[8].y
    
      middle_x=results.right_hand_landmarks.landmark[12].x
      middle_y=results.right_hand_landmarks.landmark[12].y
    
      ring_x=results.right_hand_landmarks.landmark[16].x
      ring_y=results.right_hand_landmarks.landmark[16].y
  
      pinky_x=results.right_hand_landmarks.landmark[20].x
      pinky_y=results.right_hand_landmarks.landmark[20].y
    
      wrist_x=results.right_hand_landmarks.landmark[0].x
      wrist_y=results.right_hand_landmarks.landmark[0].y
      
    # CENTER RIGHT HAND 
    center_x=(thumb_x+index_x+middle_x+ring_x+pinky_x)/5
    center_y=(thumb_x+index_y+middle_y+ring_y+pinky_y)/5
    
    # DISTANCE BETWEEN EVERY FINGER AND CENTER OF THE RIGHT PALM
    distance_thumb=((center_x - thumb_x)**2 + (center_y - thumb_y)**2)**0.5
    # distance_index=((center_x - index_x)**2 + (center_y - index_y)**2)**0.5  SE TI ALLONTANI MEDIAPIPE DA' PROBLEMI SOPRATTUTTO CON INDICE
    distance_middle=((center_x - middle_x)**2 + (center_y - middle_y)**2)**0.5
    distance_ring=((center_x - ring_x)**2 + (center_y - ring_y)**2)**0.5
    distance_pinky=((center_x - pinky_x)**2 + (center_y - pinky_y)**2)**0.5
    
    # TOTAL DISTANCE OF FINGER TIPS FROM PALM CENTER (*resize TO ADAPT THE PARAMETER WRT DISTANCE) (se lontana il resize influisce poco, se vicina il resize influisce di più)
    distance_tot= (distance_thumb + distance_middle + distance_ring +  distance_pinky)*resize_hand
    
    # THRESHOLD FOR OPEN/CLOSE RESIZED
    treshold=0.2*resize_hand   # si può modificare 0.2 o al massimo aggiungere indice, con 0.2 e senza indice a me dà i risultati migliori
    
    if distance_tot<treshold:
      open_close = 0 #hand is closed
    else:
      open_close = 1 #hand is open
      
    # 5) GRADUAL OPENING THE RIGHT HAND (*resize ALREADY DONE IN distance_tot) (O.25 IS THE NORMALIZATION), per adesso dà valori - considerando la distanza - tra 0.3 e 0.85
    distance_tot_norm= (distance_tot)/0.25
    if distance_tot_norm>1:
        distance_tot_norm=1

    # 6) ROTATION OF THE RIGHT HAND
    coord_x_right = middle_x - wrist_x
    coord_y_right = middle_y - wrist_y
    right_hand_angle = abs(math.atan2(coord_x_right, coord_y_right))/math.pi
    
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
    hand_expansion= ((((right_wrist_x-left_wrist_x)**2 + (right_wrist_x-left_wrist_y)**2)**0.5))*resize
    # hand_expansion= (((center_right_hand_x-center_left_hand_x)**2 + (center_right_hand_y-center_left_hand_y)**2)**0.5)/abs(center_head)
    if hand_expansion>1:
        hand_expansion=0.5
        
    # TO CALCULATE HEAD AND HAND SPEED
    frame_distance_hand=((((right_wrist_x-previous_right_hand_x)**2 + (right_wrist_y-previous_right_hand_y)**2)**0.5))
    frame_distance_left_hand=((((left_wrist_x-previous_left_hand_x)**2 + (left_wrist_y-previous_left_hand_y)**2)**0.5))
    frame_distance_head=((((center_head_x-previous_head_x)**2 + (center_head_y-previous_head_y)**2)**0.5))
    
     # UPDATES HEAD PREVIOUS FRAME 
    previous_head_x= center_head_x
    previous_head_y= center_head_y
     # UPDATES HAND PREVIOUS FRAME
    previous_right_hand_x= right_wrist_x
    previous_right_hand_y= right_wrist_y
    prevgray = gray
    
     # End time
    end = time.time()
    frame_time=end-start
    
    # 9) CLIPPING RIGHT HAND SPEED & ACCELERATION
    velocity_norm_right_hand=((frame_distance_hand/frame_time)/2)   #*resize_hand???
    if velocity_norm_right_hand>1:
       velocity_norm_right_hand=1
    
    deltaV_rightHand = ((velocity_norm_right_hand - previous_right_hand_v))
    previous_right_hand_v = velocity_norm_right_hand
    
    acceleration_norm_right_hand =  (deltaV_rightHand/frame_time)/10
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

    deltaV_leftHand = ((velocity_norm_left_hand - previous_left_hand_v))
    previous_left_hand_v = velocity_norm_left_hand
    
    acceleration_norm_left_hand = (deltaV_leftHand/frame_time)/10
    if acceleration_norm_left_hand>1:
       acceleration_norm_left_hand=1
    
        
    # PRINT DESIRED PARAMETER TO SEE VALUES
    #print(f"\rRight hand's speed: {velocity_norm_right_hand} ")
    #print(f"\rRight hand's acceleration: {acceleration_norm_right_hand} ")
    #print(f"\rLeft hand's acceleration: {acceleration_norm_left_hand} ")
    #print(f"\rHead's acceleration: {acceleration_head} ")
    #print(f"\rHead's speed: {velocity_norm_head} ", end='', flush=True)
    #print(f"\rRight hand is open/close: {open_close} ", end='', flush=True)
    #print(f"\rHands' expansion: {hand_expansion} ")
    #print(f"\rAverage hands' height: {hands_mean_y} ")
    # print(f"\rRight hand's rotation: {right_hand_angle} ", end='', flush=True)
    #print(f"\rRight hand's gradual opening: {distance_tot_norm}")
    #print(f"\rDistance from camera: {resize} ")
    #print(f"\rDistance of right hand from camera: {resize_hand} ")
    #print(f"\rMean direction of body's movement: {norm_ang} ", end='', flush=True)
    #print(f"\rMean magnitude of body's movement:: { norm_mag} ", end='', flush=True)
    
    
    # REMOVE ELEMENTS FROM UI
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
            client_Max8.send_message("/body/hands_HeightAVG",hands_mean_y)
            #client_Max8.send_message("/body/hands_xaxisAVG",hands_mean_x)
            #Right Hand 
            client_Max8.send_message("/body/RH_OpenClose", open_close)
            client_Max8.send_message("/body/RH_Speed", velocity_norm_right_hand)
            #client_Max8.send_message("/body/RH_Acceleration", acceleration_norm_right_hand)
            client_Max8.send_message("/body/RH_Expansion", hand_expansion)
            client_Max8.send_message("/body/RH_Rotation", right_hand_angle)
            client_Max8.send_message("/body/RH_GradualOpening", distance_tot_norm)
            client_Max8.send_message("/body/RH_camDistance", resize_hand)
            
            #Left Hand
            #client_Max8.send_message("/body/LH_Speed",  velocity_norm_left_hand)
            #client_Max8.send_message("/body/LH_Acceleration",acceleration_norm_left_hand)
            #client_Max8.send_message("/body/LH_Expasion", hand_expansion)
            #client_Max8.send_message("/body/LH_Rotation", right_hand_angle)
          
            #Head
            client_Max8.send_message("/body/H_Speed", velocity_norm_head)
            #client_Max8.send_message("/body/H_Acceleration", acceleration_head)
            client_Max8.send_message("/body/H_camDistance", resize)
            client_Max8.send_message("/body/H_centerX", center_head_x)
            client_Max8.send_message("/body/H_centerY", center_head_y)
            
            #Body
            client_Max8.send_message("/body/bodyDirection", norm_ang)
            client_Max8.send_message("/body/bodyVelocity", norm_mag)
            
            client_MusicVAE.send_message("/filter1", [1., 2.])
            '''
            #MESSAGES TO MUSIC VAE
            client_MusicVAE.send_message("/body/hands_HeightAVG",hands_mean_y)
            #Right Hand 
            client_MusicVAE.send_message("/body/RH_OpenClose", open_close)
            client_MusicVAE.send_message("/body/RH_Speed", velocity_norm_right_hand)
            client_MusicVAE.send_message("/body/RH_Acceleration", acceleration_norm_right_hand)
            client_MusicVAE.send_message("/body/RH_Expasion", hand_expansion)
            client_MusicVAE.send_message("/body/RH_Rotation", right_hand_angle)
            client_MusicVAE.send_message("/body/RH_GradualOpening", distance_tot_norm)
            client_MusicVAE.send_message("/body/RH_camDistance", resize_hand)
            
            #Left Hand
            client_MusicVAE.send_message("/body/LH_Speed",  velocity_norm_left_hand)
            #client_MusicVAE.send_message("/body/LH_Acceleration",acceleration_norm_left_hand)
            client_MusicVAE.send_message("/body/LH_Expasion", hand_expansion)
            client_MusicVAE.send_message("/body/LH_Rotation", right_hand_angle)
          
            #Head
            client_MusicVAE.send_message("/body/H_Speed", velocity_norm_head)
            client_MusicVAE.send_message("/body/H_Acceleration", acceleration_head)
            client_MusicVAE.send_message("/body/H_camDistance", resize)
            
            #Body
            client_MusicVAE.send_message("/body/bodyDirection", norm_ang)
            client_MusicVAE.send_message("/body/bodyVelocity", norm_mag)
            '''
            
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