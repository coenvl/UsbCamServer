from camera import Camera
from handler import CameraHandler

import SimpleHTTPServer
import SocketServer

PORT = 8080

#cam = Camera()
#cam.saveFrame("test.jpg")

httpd = SocketServer.TCPServer(("", PORT), CameraHandler)

try:
	httpd.serve_forever()
except KeyboardInterrupt:
	httpd.socket.close()

