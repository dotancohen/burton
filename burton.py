#!/usr/bin/python3
import os
import platform
import sys
import time

import system_statistics
import configure_websites



burton_version = '0.1'



env = ''



class Environment:
	def __init__(self):
		self.start = int(time.time())
		self.prompt = ">> "

	def changePrompt(self, prompt):
		self.prompt = prompt



def main(argv):
	global burton_version, env

	#env = Environment()
	print("\nWelcome to Burton " + burton_version + "!")

	while True:

		print("\nPlease select an operation:")
		print(" 1. System statistics")
		print(" 2. Configure websites")
		# print(" 3. Configure databases")
		# print(" 4. Configure email")
		print(" -. Exit")

		operation = input(env.prompt)

		if operation == '-':
			sys.exit()
		elif operation == '1':
			system_statistics.select_system_statistics(env)
		elif operation == '2':
			configure_websites.select_configure_websites(env)
		else:
			print("Invalid input!")



if __name__ == '__main__':

	env = Environment()

	if not os.getuid()==0:
		print("\nBurton may not run properly when not run as root.")
		print("Please exit and restart as root user or with sudo.")
		print("Using !! prompt to indicate non-root status.")
		env.changePrompt("!! ")

	main(sys.argv)
