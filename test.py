#!/usr/bin/python

from camera import Camera
from handler import CameraHandler

import SimpleHTTPServer
import SocketServer

PORT = 8081

httpd = SocketServer.TCPServer(("", PORT), CameraHandler)

try:
	httpd.serve_forever()
except KeyboardInterrupt:
	httpd.socket.close()

