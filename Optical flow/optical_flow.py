
import cv2 as cv
import numpy as np

# PRESS q TO END THE SCRIPT
# TO CALCULATE HOW MUCH MOTION THERE IS IN THE FRAME

# The video feed is read in as a VideoCapture object
cap = cv.VideoCapture(0)

# ret = a boolean return value from getting the frame
# first_frame = the first frame in the entire video sequence
ret, first_frame = cap.read()

# Converts frame to grayscale because we only need the luminance channel for
# detecting edges - less computationally expensive
prev_gray = cv.cvtColor(first_frame, cv.COLOR_BGR2GRAY)

# Creates an image filled with zero intensities with the same dimensions as the frame
mask = np.zeros_like(first_frame)

# Sets image saturation to maximum
mask[..., 1] = 255

while(cap.isOpened()):
	
	# ret = a boolean return value from gettingthe frame 
    # frame = the current frame being projected in the video
	ret, frame = cap.read()
	
	# Converts each frame to grayscale - we previously only converted the first frame to grayscale
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	
	# Calculates dense optical flow by Farneback method
    # https://docs.opencv.org/3.4/dc/d6b/group__video__track.html#ga5d10ebbd59fe09c5f650289ec0ece5af 
	flow = cv.calcOpticalFlowFarneback(prev_gray, gray ,None, 0.5, 3, 15, 3, 5, 1.1, 0)
    
    # COLORS
	# Computes the magnitude and angle of the 2D vectors <---- magnitude
	magnitude, angle = cv.cartToPolar(flow[..., 0], flow[..., 1])
 
	# Sets image color according to the optical flow direction  <---- direction
	mask[..., 0] = angle * 180 / np.pi / 2
	
	# Sets image value according to the optical flow magnitude (normalized)  <normalized magnitude
	mask[..., 2] = cv.normalize(magnitude, None, 0, 255, cv.NORM_MINMAX)
	
	# Converts HSV to RGB (BGR) color representation
	rgb = cv.cvtColor(mask, cv.COLOR_HSV2BGR)
	
	# Opens a new window and displays the output frame
	cv.imshow("dense optical flow", cv.flip(rgb,1))
	
	# Updates previous frame
	prev_gray = gray
	
    # Flip the image horizontally for a selfie-view display.

	# Frames are read by intervals of 1 millisecond. The
	# programs breaks out of the while loop when the
	# user presses the 'q' key
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

# The following frees up resources and
# closes all windows
cap.release()
cv.destroyAllWindows()
