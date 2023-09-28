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
Max8_IP_port=7400

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

#BUFFERS
bufferMag=np.zeros(50)
bufferExp=np.zeros(300)
bufferX=np.zeros(300)  
bufferY=np.zeros(300)
bufferOC=np.zeros(20) 

epsilon=10^(-3)   #vd
 
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
    
    # 1) MEAN NORMALIZED MAGNITUDE: MEAN VELOCITY OF THE WHOLE MOVEMENT IN THE SCREEN 
    #norm_mag=float(np.average(magnitude,weights = angle))  
    avg_mag=float(np.average(magnitude))
    # CLIPPING OPTICAL FLOW VELOCITY
    #if norm_mag>1:
    #  norm_mag=1 
    # UPDATE BUFFER FOR OPTICAL FLOW VELOCITY TO SMOOTH VALUES
    bufferMag=bufferMag[:-1]
    bufferMag=np.append(avg_mag, bufferMag)
    maxMag=np.max(bufferMag)
    minMag=np.min(bufferMag)
    meanMagnitude=np.mean(bufferMag[:10])
    valueMag=(meanMagnitude-minMag)/(maxMag-minMag+epsilon)
    #print(valueMag)


    # DEPTH OF THE HEAD AND OF THE RIGHT WRIST (used also to adapt parameters wrt the distance from camera)
    if not results.pose_landmarks:
      continue
    
    #head_depth= results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].z 
    #right_wrist_depth= results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].z
    # IMPORTANT: "RESIZE" PARAMETER WRT DISTANCE, DEPTH NORMALIZATION ("head_depth" is pretty linear --> variation of 1 means variation of 0,6 meters in depth, variation of 2 means variation of 1,20 meters in this way *0.6 converts the number in meters, do not touch /2 (2 maximum distance perceived) gives a normalization of distance, a percentage of how much you are distant)
    # resize=((3-abs(head_depth))*(0.6))/2
    # /1.7 (1.7 maximum distance perceived) gives a normalization of distance, a percentage of how much you are distant
    # resize_hand=((3-abs(right_wrist_depth))*(0.6))/(1.7)
    
    # RIGHT HAND LANDMARKS
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
    
      right_wrist_x=0
      right_wrist_y=0
    
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
    
      right_wrist_x=results.right_hand_landmarks.landmark[0].x
      right_wrist_y=results.right_hand_landmarks.landmark[0].y
      
    # RIGHT HAND CENTER 
    center_x=(right_thumb_x+right_index_x+right_middle_x+right_ring_x+right_pinky_x)/5
    center_y=(right_thumb_y+right_index_y+right_middle_y+right_ring_y+right_pinky_y)/5
    
    # DISTANCE BETWEEN EVERY FINGER AND CENTER OF THE RIGHT PALM
    distance_thumb=((center_x - right_thumb_x)**2 + (center_y - right_thumb_y)**2)**0.5
    # distance_index=((center_x - index_x)**2 + (center_y - index_y)**2)**0.5  
    distance_middle=((center_x - right_middle_x)**2 + (center_y - right_middle_y)**2)**0.5
    distance_ring=((center_x - right_ring_x)**2 + (center_y - right_ring_y)**2)**0.5
    distance_pinky=((center_x - right_pinky_x)**2 + (center_y - right_pinky_y)**2)**0.5
    
    # TOTAL DISTANCE OF FINGER TIPS FROM PALM CENTER  
    distance_tot= (distance_thumb + distance_middle + distance_ring + distance_pinky)
    
    # LEFT HAND LANDMARKS
    if not results.left_hand_landmarks:
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
    
      left_wrist_x=0
      left_wrist_y=0
    
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
    
      left_wrist_x=results.left_hand_landmarks.landmark[0].x
      left_wrist_y=results.left_hand_landmarks.landmark[0].y
    
    # 2) GRADUAL OPENING OF THE HAND
    bufferOC=bufferOC[:-1]
    bufferOC=np.append(distance_tot, bufferOC)
    maxOC=np.max(bufferOC)
    minOC=np.min(bufferOC)
    valueOC=(distance_tot-minOC)/(maxOC-minOC+epsilon)
    #print(valueOC)
    
    # 3) OPEN/CLOSE
    if valueOC>0.4:
      open_close=1
      #print("Open")
    else: 
      open_close=0
      #print("Closed")
      
    # 4) ROTATION OF THE RIGHT HAND
    coord_x_right = right_middle_x - right_wrist_x
    coord_y_right = right_middle_y - right_wrist_y
    right_hand_angle = abs(math.atan2(coord_x_right, coord_y_right))/math.pi
    #if right_hand_angle==0:   OPPURE 1-abs(...)
    #  right_hand_angle=1
    #print(right_hand_angle)
    
    # 5) ROTATION OF THE LEFT HAND
    coord_x_left = left_middle_x - left_wrist_x
    coord_y_left = left_middle_y - left_wrist_y
    left_hand_angle = abs(math.atan2(coord_x_left, coord_y_left))/math.pi
    #if left_hand_angle==0:
    #  left_hand_angle=1
    #print(left_hand_angle)
    
    # 6) HANDS HEIGHT --> MIDDLE POINT BETWEEN WRISTS
    hands_mean_y= ((left_wrist_y+right_wrist_y)/2)   #*resize
    #if not results.left_hand_landmarks:....
    #  hands_mean_y=0.5
    #if hands_mean_y>1:
    #  hands_mean_y=1 
    #if hands_mean_y<0:
    #  hands_mean_y=0 
    #print(hands_mean_y)
    bufferY=bufferY[:-1]
    bufferY=np.append(hands_mean_y, bufferY)
    maxY=np.max(bufferY)
    minY=np.min(bufferY)
    meanY=np.mean(bufferY[:15])
    valueY=1-((meanY-minY)/(maxY-minY+epsilon))   #vd. se 1-
    #print(valueY)
    
    # 7) HANDS x
    hands_mean_x= ((left_wrist_x+right_wrist_x)/2)  #*resize
    #if hands_mean_x>1:
    #    hands_mean_x=1 
    #if hands_mean_x<0:
    #    hands_mean_x=0 
    #print(hands_mean_x)
    bufferX=bufferX[:-1]
    bufferX=np.append(hands_mean_x, bufferX)
    maxX=np.max(bufferX)
    minX=np.min(bufferX)
    meanX=np.mean(bufferX[:15])
    valueX=1-((meanX-minX)/(maxX-minX+epsilon))   #invalid value encountered in double_scalars
    #print(valueX)
    
    # 8) HANDS EXPANSION  --> EUCLIDEAN DISTANCE BETWEEN HANDS 
    hand_expansion= ((((right_wrist_x-left_wrist_x)**2 + (right_wrist_y-left_wrist_y)**2)**0.5))    #*resize
    # hand_expansion= (((center_right_hand_x-center_left_hand_x)**2 + (center_right_hand_y-center_left_hand_y)**2)**0.5)/abs(center_head)
    #if hand_expansion>1: 
    #    hand_expansion=1
    
    bufferExp=bufferExp[:-1]
    bufferExp=np.append(hand_expansion, bufferExp)
    minExp=np.min(bufferExp)
    maxExp=np.max(bufferExp)
    meanExp=np.mean(bufferExp[:15])
    valueExp=(meanExp-minExp)/(maxExp-minExp+epsilon)
    print(valueExp)
        
    prevgray = gray
    
     # End time
    end = time.time()
    frame_time=end-start
    
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
            #client_Max8.send_message("/body/flow", meanMagnitude)             #1
            client_Max8.send_message("/body/opening", valueOC)                #2 
            client_Max8.send_message("/body/open_close", open_close)          #3
            client_Max8.send_message("/body/RH_rotation", right_hand_angle)   #4   
            client_Max8.send_message("/body/LH_Rotation", left_hand_angle)    #5
            client_Max8.send_message("/body/hands_y",valueY)                  #6
            client_Max8.send_message("/body/hands_x",valueX)                  #7
            client_Max8.send_message("/body/hands_expansion",valueExp)        #8
  
            '''
            #MESSAGES TO MUSIC VAE
            client_MusicVAE.send_message("/filter1", [1., 2.])
            client_MusicVAE.send_message("/body/flow", meanMagnitude)             #1
            client_MusicVAE.send_message("/body/opening", valueOC)                #2 
            client_MusicVAE.send_message("/body/open_close", open_close)          #3
            client_MusicVAE.send_message("/body/RH_rotation", right_hand_angle)   #4   
            client_MusicVAE.send_message("/body/LH_Rotation", left_hand_angle)    #5
            client_MusicVAE.send_message("/body/hands_y",valueY)                  #6
            client_MusicVAE.send_message("/body/hands_x",valueX)                  #7
            client_MusicVAE.send_message("/body/hands_x",valueExp)                #8
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