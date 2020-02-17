import cv2
import numpy as np

##########################################
'''
Parameters for camera
'''
rx = 640        #resolution for X
ry = 480        #resolution for Y
cx = rx//2		#principal point for X
cy = ry//2		#principal point for Y

##########################################
'''
Define functions
'''
def event_callback(event,x,y,flages,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print "X :", x, ", Y : ", y

def capture_test():
	cam = cv2.VideoCapture(0)
	cam.set(3, rx)
	cam.set(4, ry)
	
	cv2.namedWindow('Video Test')
	cv2.setMouseCallback('Video Test', event_callback)
	
	while True:
		_, frame = cam.read()
		cv2.imshow('Video Test', frame)
		
		if cv2.waitKey(1) & 0xFF == ord(' '):
			break
			
	cam.release()
	cv2.destroyAllWindows()
			
def image_test():
	img = cv2.VideoCapture(0)
	img.set(3, rx)
	img.set(4, ry)
	
	cv2.namedWindow('Image Test')
	cv2.setMouseCallback('Image Test', event_callback)
	
	_, frame = img.read()
	cv2.imwrite("image_test.jpg", frame)
	
	test_img = cv2.imread("image_test.jpg")
	cv2.imshow('Image Test',test_img)
	
	cv2.waitKey()
	
if __name__ == '__main__':
	#capture_test()
	image_test()
