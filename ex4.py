# save the captured frame
from cv2 import *

cam=VideoCapture(0)
while True:
	res,img=cam.read()
	if res:
		imshow('Camera Feed',img)
		t=waitKey(1)
		if(t==ord('s')):
			print ('Image Captured')
			imwrite('feed.jpg',img)
			destroyAllWindows()
			break
cam.release()