#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import logging
import os.path
import uuid
import signal
import sys
import threading
import json
import encodings
import time
import serial

import multiwii
import server

class Derp():
	def derp(self, board):
		time.sleep(6)
		while  1:
			time.sleep(0.1)
			board.rcData = [
				((40/100)*500+1500),
				((40/100)*500+1500),
				((10/100)*500+1500),
				1600,
			]
			print(board.rcData)

class Main():
	def start(self, board):
		self.hello = "hello"
		test = "test"
		self.board = board

	def stop(self):
		self.board.stop()

	
if __name__ == "__main__":
	global board
	board = multiwii.drone('/dev/tty.usbserial-A8005MO9')
	
	start = Main()
	MainThread = threading.Thread(target=start.start, args=(board,))
	MainThread.start()

	derpy = Derp()
	DerpThread = threading.Thread(target=derpy.derp, args=(board,))
	DerpThread.start()
	
	def signal_handler(signal, frame):
		print('You pressed Ctrl+C!')
		start.stop()
		derpy.stop()
	
	signal.signal(signal.SIGINT, signal_handler)
	signal.pause()
