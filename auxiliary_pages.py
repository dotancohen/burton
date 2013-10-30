import os
import sys



environment = ''



def main(env):
	global environment
	environment = env

	while True:
		print("\nView Help, About, License, and Copyright pages\n")
		print("Please select an operation:")
		print(" 1. View Help page")
		print(" 2. View About page")
		print(" 3. View License page")
		print(" 4. View Copyright page")
		print(" 0. Go Back")
		print(" -. Exit")

		operation = input(environment.prompt)

		if operation == '0':
			return True
		elif operation == '-':
			sys.exit()
		elif operation == '1':
			view_help_page()
		elif operation == '2':
			view_about_page()
		elif operation == '3':
			view_license_page()
		elif operation == '4':
			view_copyright_page()
		else:
			print("Invalid input.")



def view_help_page():
	print("\nHelp page\n")
	return True



def view_about_page():
	print("\nAbout page\n")
	return True



def view_license_page():
	print("\nLicense page\n")
	return True



def view_copyright_page():
	print("\nCopyright page")
	print("""
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
	""")
	return True
