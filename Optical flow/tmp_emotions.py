import cv2 as cv
import emotion_recognition as emot
import numpy as np

er = emot.EmotionRecognition(device='cpu', gpu_id=0)

cam = cv.VideoCapture(0)

success, frame = cam.read()

frame = er.recognise_emotion(frame, return_type='BGR')

cv.imshow("frame", frame)

while True:
    key = cv.waitKey(10)
    if key & 0xff == 27:
        break

cam.release()