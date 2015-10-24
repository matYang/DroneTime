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


class Main():
	def start(self, board):
		self.hello = "hello"
		test = "test"
		self.board = board

		#delay for calibration
		init_delay = 5;
		while init_delay:
			print("command countdown: " + str(init_delay))
			time.sleep(1)
			init_delay = init_delay - 1;

		while 1:
			throttle = eval(raw_input("Enter throttle: "))
			board.rcData = [1500, 1500, 1500, throttle]


	def stop(self):
		self.board.stop()

	
if __name__ == "__main__":
	global board
	#canfind wih tail -f /var/log/messages
	board = multiwii.drone('/dev/tty.usbserial-A8005MO9')
	
	start = Main()
	MainThread = threading.Thread(target=start.start, args=(board,))
	MainThread.start()
	
	def signal_handler(signal, frame):
		print('You pressed Ctrl+C!')
		board.rcData = [1500, 1500, 1500, 1000]
		time.sleep(1)
		start.stop()
		time.sleep(1)
		sys.exit(0)
	
	signal.signal(signal.SIGINT, signal_handler)
	signal.pause()
