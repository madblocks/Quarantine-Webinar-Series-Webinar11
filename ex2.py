from cv2 import *

# Read the image
img=imread('aa.jpg',1)
imwrite('style-star.jpg',img)
imshow('style-star',img)
t=waitKey(0)
if(t==ord('q')):
	destroyAllWindows()