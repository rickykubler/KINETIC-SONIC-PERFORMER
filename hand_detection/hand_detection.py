import cv2
import imutils

from hand_detection_utils import *

if __name__ == "__main__":

    hand = None

    camera = cv2.VideoCapture(0)
    
    num_frames = 0

    # for running weight
    aweight = 0.5

    ## region of interest (ROI) coordinates
	
    top, right, bottom, left = 10, 350, 225, 590

	# Dimensions of the image considered for hand detection
	
    height_roi = bottom - top
	
    width_roi = left - right

    while True:
        # @grabbed: boolean True if frame has been grabbed
        # @frame: current frame, size (1280x720) 
        (grabbed, frame) = camera.read()

        # aspect ratio
        # link: https://pyimagesearch.com/2015/02/02/just-open-sourced-personal-imutils-package-series-opencv-convenience-functions/
        frame = imutils.resize(frame, width=700)
        # flip the frame so that it is not the mirror view
        frame = cv2.flip(frame, 1)
	    # clone the frame
        clone = frame.copy()
        # frame.shape = (525, 700, 3)
        (height, width) = frame.shape[:2]
        # get the ROI
		
        roi = frame[top:bottom, right:left]
        # convert the roi to grayscale and blur it
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
	    # https://www.tutorialkart.com/opencv/python/opencv-python-gaussian-image-smoothing/
        gray = cv2.GaussianBlur(gray, (7, 7), 0)    

        if num_frames < 30:
            run_avg(gray, aweight)
        else:
            hand = segment(gray)

            # check whether hand region is segmented
            if hand is not None:
				# if yes, unpack the thresholded image and
				# segmented region
				
                (thresholded, segmented) = hand

				# draw the segmented region and display the frame
				
                cv2.drawContours(clone, [segmented + (right, top)], -1, (0, 0, 255))
				# Center of the hand
				
                c_x, c_y = detect_palm_center(segmented)
				
                radius = 5
				
                cv2.circle(thresholded, (c_x, c_y), radius, 0, 1)
				
                cv2.imshow("Thesholded", thresholded)   
        # draw the segmented hand
		
        cv2.rectangle(clone, (left, top), (right, bottom), (0, 255, 0), 2)

		# increment the number of frames
		
        num_frames += 1    
        # display the frame with segmented hand		    
        cv2.imshow("Video Feed", clone) 

        # observe the keypress by the user
		
        keypress = cv2.waitKey(1) & 0xFF

		
		# if the user pressed "q", then stop looping
		
        if keypress == ord("q"):
			
            break

# free up memory
camera.release()
cv2.destroyAllWindows()