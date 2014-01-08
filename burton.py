#!/usr/bin/python3

"""
	Burton: CLI-based web server control panel
    Copyright (C) 2013 Dotan Cohen http://dotancohen.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    http://www.gnu.org/licenses/

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""

import os
import platform
import sys
import time

import system_statistics
import configure_system
import configure_websites
import configure_email
import install_applications
import auxiliary_pages


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
		print(" 1. Operating system statistics")
		print(" 2. Configure and maintain operating system")
		print(" 3. Configure websites")
		print(" 4. Configure email")
		print(" 5. Install applications")
		# print(" 5. Configure databases")
		print(" 9. View Help, About, License, and Copyright pages")
		print(" -. Exit")

		operation = input(env.prompt)
		operation = operation.lower().strip()

		if operation == '-':
			sys.exit()
		elif operation == '1':
			system_statistics.main(env)
		elif operation == '2':
			configure_system.main(env)
		elif operation == '3':
			configure_websites.main(env)
		elif operation == '4':
			configure_email.main(env)
		elif operation == '5':
			install_applications.main(env)
		elif operation == '9':
			auxiliary_pages.main(env)
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
