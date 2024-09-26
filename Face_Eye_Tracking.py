import cv2
import numpy as np
Capture=cv2.VideoCapture(0)
Face_Cascasde=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
Eye_Casscade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
while(True):
	ret,Frame=Capture.read()
	Gray=cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
	Faces=Face_Cascasde.detectMultiScale(Gray,1.3,5)
	for(Face_x,Face_y,Face_Width,Face_Height) in Faces:
		cv2.rectangle(Frame,(Face_x,Face_y),(Face_x+Face_Width,Face_y+Face_Height),(0,0,255),5)
		Face_Gray=Gray[Face_y:Face_y+Face_Height,Face_x:Face_x+Face_Width]
		Face_Color=Frame[Face_y:Face_y+Face_Height,Face_x:Face_x+Face_Width]
		Eyes=Eye_Casscade.detectMultiScale(Face_Gray,1.3,5)
		for(Eye_x,Eye_y,Eye_Width,Eye_Height) in Eyes:
			cv2.rectangle(Face_Color,(Eye_x,Eye_y),(Eye_x+Eye_Width,Eye_y+Eye_Height),(0,255,0),5)
	cv2.imshow('Camera',Frame)
	PressedKey=cv2.waitKey(1)
	if PressedKey==ord(' '):
		break;
	if ret==False:
		break
Capture.release()
cv2.destroyAllWindows()