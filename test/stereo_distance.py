import numpy as np
import RPi.GPIO as gp
import cv2
import os
import sys
import time
import math
import subprocess

######################################
'''
Parameter setting
'''
width  = 480 #320
height = 640 #240
fps = 30
brightness = 50               # min=0   max=100  step=1q
contrast = 0                  # min=-100  max=100  step=1
saturation = 0                # min=-100  max=100  step=1
rotate = 0                    # min=0  max=360  step=90 
auto_exposure = 0             # min=0  max=3 
exposure_time_absolute = 1000 # min = 1  max=10000  step=1

######################################
'''
GPIO initialize
'''
gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(7,gp.OUT)
gp.setup(11,gp.OUT)
gp.setup(12,gp.OUT)

######################################
'''
Functions
'''
def take_L_image():
	i2c = "i2cset -y 1 0x70 0x00 0x04"
    
	os.system(i2c)
	gp.output(7, False)
	gp.output(11, False)
	gp.output(12, True)
	
	cap = cv2.VideoCapture(0)
	'''
	cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, width)
	cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, height)
	cap.set(cv2.cv.CV_CAP_PROP_FPS, fps)   
	command ="v4l2-ctl -d 0 -c brightness=%d" % (brightness)
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c contrast=%d" % (contrast)
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c saturation=%d" % (saturation)
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c rotate=%d" % (rotate)
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c auto_exposure=%d" % (auto_exposure)
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c exposure_time_absolute=%d" % (exposure_time_absolute)
	output = subprocess.call(command, shell=True)
	'''
	rev, frame = cap.read()
	#blur_frame = cv2.GaussianBlur(frame, (5,5), 0)
	#resized_frame = cv2.resize(blur_frame, dsize=(600, 400), interpolation=cv2.INTER_AREA)
	
	cv2.imwrite('capture_L.png', frame)
    
def take_R_image():    
	i2c = "i2cset -y 1 0x70 0x00 0x06"
        
	os.system(i2c)
	gp.output(7, False)
	gp.output(11, True)
	gp.output(12, False)
    
	cap = cv2.VideoCapture(0)
	'''
	cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, width)
	cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, height)
	cap.set(cv2.cv.CV_CAP_PROP_FPS, fps)   
	command ="v4l2-ctl -d 0 -c brightness=%d" % (brightness)
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c contrast=%d" % (contrast)
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c saturation=%d" % (saturation)
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c rotate=%d" % (rotate)
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c auto_exposure=%d" % (auto_exposure)
	output = subprocess.call(command, shell=True)
	command ="v4l2-ctl -d 0 -c exposure_time_absolute=%d" % (exposure_time_absolute)
	output = subprocess.call(command, shell=True)
	'''
	rev, frame = cap.read()
	
	cv2.imwrite('capture_R.png', frame)
 
def event_callback(event,x,y,flages,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print("X :", x, ", Y : ", y)	
		
def select_coordinates():
	img_L = cv2.imread('capture_L.png')
	img_R = cv2.imread('capture_R.png')
	
	cv2.namedWindow('Left Image')
	cv2.namedWindow('Right Image')
	
	cv2.setMouseCallback('Left Image', event_callback)
	cv2.setMouseCallback('Right Image', event_callback)
	
	cv2.imshow('Left Image', img_L)
	cv2.imshow('Right Image', img_R)
	
	cv2.waitKey()
    
######################################

if __name__ == '__main__':
	take_L_image()
	take_R_image()
	select_coordinates()
