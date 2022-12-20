import cv2
import mediapipe as mp
import argparse
from pythonosc import udp_client

import numpy as np
import matplotlib.pyplot as plt

import math

def countFingers(image, results, draw=True, display=True):


    '''
    This function will count the number of fingers up for each hand in the image.
    Args:
        image:   The image of the hands on which the fingers counting is required to be performed.
        results: The output of the hands landmarks detection performed on the image of the hands.
        draw:    A boolean value that is if set to true the function writes the total count of fingers of the hands on the
                 output image.
        display: A boolean value that is if set to true the function displays the resultant image and returns nothing.
    Returns:
        output_image:     A copy of the input image with the fingers count written, if it was specified.
        fingers_statuses: A dictionary containing the status (i.e., open or close) of each finger of both hands.
        count:            A dictionary containing the count of the fingers that are up, of both hands.
    '''
    global left_hand_angle
    # Get the height and width of the input image.
    height, width, _ = image.shape
    
    # Create a copy of the input image to write the count of fingers on.
    output_image = image.copy()
    
    # Initialize a dictionary to store the count of fingers of both hands.
    count = {'RIGHT': 0, 'LEFT': 0}
    
    # Store the indexes of the tips landmarks of each finger of a hand in a list.
    fingers_tips_ids = [mpHands.HandLandmark.INDEX_FINGER_TIP, mpHands.HandLandmark.MIDDLE_FINGER_TIP,
                        mpHands.HandLandmark.RING_FINGER_TIP, mpHands.HandLandmark.PINKY_TIP]
    
    # Initialize a dictionary to store the status (i.e., True for open and False for close) of each finger of both hands.
    fingers_statuses = {'RIGHT_THUMB': False, 'RIGHT_INDEX': False, 'RIGHT_MIDDLE': False, 'RIGHT_RING': False,
                        'RIGHT_PINKY': False, 'LEFT_THUMB': False, 'LEFT_INDEX': False, 'LEFT_MIDDLE': False,
                        'LEFT_RING': False, 'LEFT_PINKY': False}


    right = ['RIGHT_THUMB', 'RIGHT_INDEX', 'RIGHT_MIDDLE', 'RIGHT_RING', 'RIGHT_PINKY']
    left = ['LEFT_THUMB', 'LEFT_INDEX', 'LEFT_MIDDLE', 'LEFT_RING', 'LEFT_PINKY']
    
    OPEN_RIGHT = False
    OPEN_LEFT = False
    wrist = mpHands.HandLandmark.WRIST 
    middle_finger_tip = mpHands.HandLandmark.MIDDLE_FINGER_TIP
    
    # Iterate over the found hands in the image.
    for hand_index, hand_info in enumerate(results.multi_handedness):
        
        
        # Retrieve the label of the found hand.
        hand_label = hand_info.classification[0].label
        
        # Retrieve the landmarks of the found hand.
        hand_landmarks =  results.multi_hand_landmarks[hand_index]



        if hand_label == 'Left':
            coord_x_left = hand_landmarks.landmark[middle_finger_tip].x - hand_landmarks.landmark[wrist].x
            coord_y_left = hand_landmarks.landmark[middle_finger_tip].y - hand_landmarks.landmark[wrist].y

            left_hand_angle = abs(math.atan2(coord_x_left, coord_y_left))/math.pi
        
        # Iterate over the indexes of the tips landmarks of each finger of the hand.
        for tip_index in fingers_tips_ids:
            
            # Retrieve the label (i.e., index, middle, etc.) of the finger on which we are iterating upon.
            finger_name = tip_index.name.split("_")[0]
            
            # Check if the finger is up by comparing the y-coordinates of the tip and pip landmarks.
            if (hand_landmarks.landmark[tip_index].y < hand_landmarks.landmark[tip_index - 2].y):
                
                # Update the status of the finger in the dictionary to true.
                fingers_statuses[hand_label.upper()+"_"+finger_name] = True
                
                # Increment the count of the fingers up of the hand by 1.
                count[hand_label.upper()] += 1
        
        # Retrieve the y-coordinates of the tip and mcp landmarks of the thumb of the hand.
        thumb_tip_x = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP].x
        thumb_mcp_x = hand_landmarks.landmark[mpHands.HandLandmark.THUMB_TIP - 2].x

        
        # Check if the thumb is up by comparing the hand label and the x-coordinates of the retrieved landmarks.
        if (hand_label=='Right' and (thumb_tip_x < thumb_mcp_x)) or (hand_label=='Left' and (thumb_tip_x > thumb_mcp_x)):
            
            # Update the status of the thumb in the dictionary to true.
            fingers_statuses[hand_label.upper()+"_THUMB"] = True
            
            # Increment the count of the fingers up of the hand by 1.
            count[hand_label.upper()] += 1

        for key in right:
            if fingers_statuses.get(key):
                OPEN_RIGHT = True
            
        for key in left:
            if fingers_statuses.get(key):
                OPEN_LEFT = True

    # Check if the total count of the fingers of both hands are specified to be written on the output image.
    if draw:

        # Write the total count of the fingers of both hands on the output image.
        cv2.putText(output_image, " Total Fingers: ", (10, 25),cv2.FONT_HERSHEY_COMPLEX, 1, (20,255,155), 2)
        cv2.putText(output_image, str(sum(count.values())), (width//2-150,240), cv2.FONT_HERSHEY_SIMPLEX,
                    8.9, (20,255,155), 10, 10)

    # Check if the output image is specified to be displayed.
    if display:
        
        # Display the output image.
        plt.figure(figsize=[10,10])
        plt.imshow(output_image[:,:,::-1]);plt.title("Output Image");plt.axis('off')
    
    # Otherwise
    else:

        # Return the output image, the status of each finger and the count of the fingers up of both hands.
        return output_image, fingers_statuses, count, OPEN_RIGHT, OPEN_LEFT, left_hand_angle

def set_client():
    # start the osc
    # argparse helps writing user-friendly commandline interfaces
    parser = argparse.ArgumentParser()
    # OSC server ip: '127.0.0.1'
    #parser.add_argument("--ip", default='192.168.255.27', help="The ip of the OSC server")
    parser.add_argument("--ip", default='127.0.0.1', help="The ip of the OSC server") # if in the same machine
    parser.add_argument("--port", type=int, default=7500, help="The port the OSC server is listening on")

    # Parse the arguments
    args, unknown = parser.parse_known_args()

    # Start the UDP Client
    return udp_client.SimpleUDPClient(args.ip, args.port)

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

START_SOUND = True
# start the osc
# argparse helps writing user-friendly commandline interfaces
parser = argparse.ArgumentParser()
# OSC server ip: '127.0.0.1'
#parser.add_argument("--ip", default='192.168.255.27', help="The ip of the OSC server")
parser.add_argument("--ip", default='127.0.0.1') # if in the same machine
parser.add_argument("--port", type=int, default=7400)

# Parse the arguments
args, unknown = parser.parse_known_args()

# Start the UDP Client
client = udp_client.SimpleUDPClient(args.ip, args.port)


parser_2 = argparse.ArgumentParser()
# OSC server ip: '127.0.0.1'
#parser_2.add_argument("--ip", default='192.168.255.27', help="The ip of the OSC server")
parser_2.add_argument("--ip", default='127.0.0.1') # if in the same machine
parser_2.add_argument("--port", type=int, default=7500)

# Parse the arguments
args_2, unknown = parser_2.parse_known_args()

# Start the UDP Client
client_2 = udp_client.SimpleUDPClient(args_2.ip, args_2.port) 

OPEN_RIGHT = False
OPEN_LEFT = False
center_x = []
center_y = []
left_hand_angle = 0
while True:
    success, image = cap.read()
    image = cv2.flip(image, 1)
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    
    # checking whether a hand is detected
    if results.multi_hand_landmarks:
        # Count the number of fingers up of each hand in the frame.
        image, fingers_statuses, count, OPEN_RIGHT, OPEN_LEFT, left_hand_angle = countFingers(image, results, display=False, draw=False)

        for hand_index, handLms in enumerate(results.multi_hand_landmarks): # working with each hand
            hand_headness = results.multi_handedness[hand_index]
            hand_label = hand_headness.classification[0].label

            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                # helps to extract the center coordinates
                if(id == 0 or id == 5 or id == 17):
                    center_x.append(cx)
                    center_y.append(cy)
            
            if hand_label == "Right":
                center_palm_x_right = sum(center_x)/(len(center_x)*w)
                center_palm_y_right = sum(center_y)/(len(center_y)*h)
            int_palm_x = int(sum(center_x)/len(center_x))
            int_palm_y = int(sum(center_y)/len(center_y))
            cv2.circle(image, (int_palm_x, int(int_palm_y)), 10, (0, 255 ,255), cv2.FILLED)

            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
            center_x = []
            center_y = []
            
        if START_SOUND:
            #print(center_palm_y)
            client.send_message("freq", center_palm_y_right)
            client_2.send_message("freq", center_palm_y_right)

            client.send_message("amp", center_palm_x_right)
            client_2.send_message("amp", center_palm_x_right)
            

            client.send_message("fx", left_hand_angle)
            client_2.send_message("fx", left_hand_angle)
            #print(left_hand_angle)

            if OPEN_RIGHT and not prev_state:
                client.send_message("on_off", 1)
                client_2.send_message("on_off", 1)
                print('on')
            elif not OPEN_RIGHT and prev_state:
                client.send_message("on_off", 0)
                client_2.send_message("on_off", 0)
                print('off')

    prev_state = OPEN_RIGHT

    cv2.imshow("Output", image)
    cv2.waitKey(1)
    
    keypress = cv2.waitKey(1) & 0xFF		
    if keypress == ord("q"):
		    break

# free up memory
cap.release()
cv2.destroyAllWindows()

client.send_message("on_off", 0)
#client_2.send_message("on_off", 0)