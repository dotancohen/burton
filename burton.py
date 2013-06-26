#!/usr/bin/python3
import os
import platform
import sys
import time

import system_statistics
import configure_websites



burton_version = '0.1'



def main(argv):
	global burton_version

	print("\nWelcome to Burton " + burton_version + "!")

	while True:

		print("\nPlease select an operation:")
		print(" 1. System statistics")
		print(" 2. Configure websites")
		# print(" 3. Configure databases")
		# print(" 4. Configure email")
		print(" 0. Exit")

		operation = input(">> ")

		if operation == '0':
			sys.exit()
		elif operation == '1':
			system_statistics.select_system_statistics()
		elif operation == '2':
			configure_websites.select_configure_websites()
		else:
			print("Invalid input!")



if __name__ == '__main__':
	main(sys.argv)
	""" Reenable after development is done!
	if os.getuid()==0:
		main(sys.argv)
	else:
		print("Please run as root.")
	"""
