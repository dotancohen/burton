import os
import sys



environment = ''



def main(env):
	global environment
	environment = env

	while True:
		print("\nInstall applications\n")
		print("Please select an operation:")
		print(" 1. Install webserver components")
		print(" 2. Install mail server components")
		print(" 0. Go Back")
		print(" -. Exit")

		operation = input(environment.prompt)

		if operation == '0':
			return True
		elif operation == '-':
			sys.exit()
		elif operation == '1':
			install_webserver()
		elif operation == '2':
			install_mailserver()
		else:
			print("Invalid input.")



def install_webserver():
	print("Install webserver!")
	return True



def install_mailserver():
	print("Install mail server!")
	return True
