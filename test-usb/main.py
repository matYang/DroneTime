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

		time.sleep(1)
		throt = 100
		while 1:
			throt += 100
			board.rcData = [1400 + throt % 500, 1200 + throt % 500, 1100 + throt % 500, 1000 + throt % 500]


	def stop(self):
		self.board.stop()

	
if __name__ == "__main__":
	global board
	board = multiwii.drone('/dev/tty.usbserial-A8005MO9')
	
	start = Main()
	MainThread = threading.Thread(target=start.start, args=(board,))
	MainThread.start()
	
	def signal_handler(signal, frame):
		print('You pressed Ctrl+C!')
		start.stop()
		sys.exit(0)
	
	signal.signal(signal.SIGINT, signal_handler)
	signal.pause()
