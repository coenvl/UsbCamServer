from StringIO import StringIO

import cv2
from PIL import Image


class Camera(object): 
	def __init__(self): #, camid, size, fps)
		self.cam = cv2.VideoCapture(0);
		self.cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 800);
		self.cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 600);
		#self.cam.set(cv2.CAP_PROP_FPS, 30)

	def getFrame(self):
		if not self.cam.isOpened():
			return '';
		
		ret, frame = self.cam.read()
		image = Image.fromarray(frame)
		return image
		#buf = StringIO()
		#image.save(buf, 'JPEG')
		#return buf.getValue();
	
	def saveFrame(self, file):
		ret, frame = self.cam.read()
		cv2.imwrite(file, frame)
