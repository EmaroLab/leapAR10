#!/usr/bin/env python

import time
import sys
import os
import argparse
from ros_ar10_class import ar10

if __name__ == "__main__":
	""" Send command to open/close AR10

	This script is provided initially by Active Robots
	and slightly Modified in order to adapt it for using two hands at the same time

	This script is used to calculate the errors for each joint

	:Arguments:
	`--device` (string) - path of the serial device connected with AR10
	`--left/--right` (flag) - command will be sent for left hand or right hand
	`--open/--close` (flag) - command AR10 to open or close
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--device', dest="device", required=True, help="serial device")
	hand_group = parser.add_mutually_exclusive_group(required=True)
	hand_group.add_argument('-l', '--left', dest="left", help = "use left hand",action='store_true')
	hand_group.add_argument('-r', '--right', dest="right", help = "use right hand",action='store_true')
	hand_group = parser.add_mutually_exclusive_group(required=True)
	hand_group.add_argument('-o', '--open', dest="open", help = "open hand",action='store_true')
	hand_group.add_argument('-c', '--close', dest="close", help = "close hand",action='store_true')
	args = parser.parse_args()
	file_path = os.path.dirname(os.path.realpath(__file__)) + "/ros_ar10_calibration_file"
	if args.left: #if conditions relating to corresponding arguments
		file_path = file_path + ".left"
	if args.right: #if conditions relating to corresponding arguments
		file_path = file_path + ".right"
	file_path = file_path
	device_path = args.device
	hand = ar10(device_path, file_path)
	if args.open:
		hand.open_hand()
	if args.close:
		hand.close_hand()
	hand.close()
