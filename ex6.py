# Mask the image with yellow - removing yellow from the image

import cv2
import numpy as np

while True:
	img=cv2.imread('aa.jpg',1) # H-Hue, S-Saturation, V-Value
	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	
	lower_yellow=np.array([20,100,100])
	upper_yellow=np.array([30,255,255])
	
	mask=cv2.inRange(hsv,lower_yellow, upper_yellow)
	res=cv2.bitwise_and(img,img,mask=mask)
	cv2.imshow('img',img)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	k=cv2.waitKey(0)
	if(k==ord('q')):
		cv2.destroyAllWindows()
		break
	