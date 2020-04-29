from cv2 import *

img=imread('aa.jpg',1) # Shape gives you the dimensions of image
o_width=img.shape[1]
o_height=img.shape[0]

r_width=o_width
r_height=o_height

while True:
	print ('Press 1 for Zoom In')
	print ('Press  2 for Zoom Out')
	print ('Press 3 for exit')
	n=int(input('Enter Choice: '))
	if(n==1):
		r_width=int(r_width+(r_width*0.1))
		r_height=int(r_height+(r_height*0.1))
		dm=(r_width,r_height)
		resized=resize(img,dm)
		imshow('Resized Image', resized)
		t=waitKey(0)
		destroyAllWindows()
	elif(n==2):
		r_width=int(r_width-(r_width*0.1))
		r_height=int(r_height-(r_height*0.1))
		dm=(r_width,r_height)
		resized=resize(img,dm)
		imshow('Resized Image',resized)
		t=waitKey(0)
		destroyAllWindows()
	else:
		break