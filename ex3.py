# Capture Image through Camera

from cv2 import *

cam=VideoCapture(0) # camera-id 

while True:
	res,img=cam.read()
	if res: # res -0 when frame is not capture, res-1
		imshow('Camera Feed',img)
		t=waitKey(1)
		if(t==ord('q')):
			destroyAllWindows()
			break

cam.release()
			