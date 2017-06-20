import time
import subprocess
from camera import Camera
from BaseHTTPServer import BaseHTTPRequestHandler
from ffmpy import FFmpeg

class CameraHandler(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
	self.cam = Camera()
	BaseHTTPRequestHandler.__init__(self, request, client_address, server)
	

    def do_GET(self):
	if (self.path == "/cam.jpg"):	
        	self.send_response(200)
       		self.send_header("Content-type", "image/jpg")
        	self.end_headers()
		self.cam.getFrame().save(self.wfile, "JPEG")
	if (self.path == "/cam.mp4"):
		self.send_response(200)

	        self.send_header("Cache-Control", "no-cache" )
    	    	self.send_header("Pragma", "no-cache" )
       	 	self.send_header("Connection", "close" )
       		self.send_header("Content-type", "video/webm")

		self.end_headers()

		ff = FFmpeg(inputs={'test.mp4': None}, outputs={'pipe:1': '-c:v h264 -f avi'})
		stdout, stderr = ff.run(stdout=self.wfile)
		

	if (self.path == "/cam.mjpg"):
		self.send_response(200)

	        self.send_header( "Cache-Control", "no-cache" )
    	    	self.send_header( "Pragma", "no-cache" )
       	 	self.send_header( "Connection", "close" )
       		self.send_header( "Content-Type", "multipart/x-mixed-replace; boundary=--myboundary" )	

        	self.end_headers()
		
		minDelay = 1.0 / 30

		lastFrameTime = 0;
		while True:
			if lastFrameTime != 0:
				delay = time.time() - lastFrameTime
				if (delay < minDelay):
					time.sleep(minDelay - delay)

			try:
				self.wfile.write( "--myboundary\r\n" )
                    		self.wfile.write( "Content-Type: image/jpeg\r\n" )
                    		#self.wfile.write( "Content-Length: %s\r\n" % len(contents) )
                    		self.wfile.write( "\r\n" )
				self.cam.getFrame().save(self.wfile, "JPEG")
                    		self.wfile.write( "\r\n" )
			except:
				print "Finished serving client"
				return

			lastFrameTime = time.time()


