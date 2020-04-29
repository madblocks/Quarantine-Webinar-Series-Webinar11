# Reading Image 'aa.jpg' and showing it to the user
from cv2 import * # cv2 - module name 

while True:
	print ('Press 1 for Reading in Color')
	print ('Press 2 for Reading in Grayscale')
	print ('Press 3 for exit')
	n=int(input('Enter Choice: '))
	if(n==1):
		print ('Reading in Color Format')
		img=imread('aa.jpg',1) # reads the image
		imshow('Color Image',img) # show the image
		t=waitKey(0) # wait until a key pressed, if it is pressed then that value will be stored in t.
		if(t==ord('q')): 
			destroyAllWindows()
	elif(n==2):
		print ('Reading in Grayscale Format')
		img=imread('aa.jpg',0)
		imshow('Grayscale Image',img)
		t=waitKey(0)
		if(t==ord('q')):
			destroyAllWindows()
	else:
		break
			
