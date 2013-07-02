import os
import sys



environment = ''



def select_configure_email(env):
	global environment
	environment = env

	while True:
		print("\nConfigure Email\n")
		print("Please select an operation:")
		print(" 1. Manage email accounts")
		print(" 2. Manage email forwarders")
		print(" 0. Go Back")
		print(" -. Exit")

		operation = input(environment.prompt)

		if operation == '0':
			return True
		elif operation == '-':
			sys.exit()
		elif operation == '1':
			manage_email_accounts()
		elif operation == '2':
			manage_email_forwarders()
		else:
			print("Invalid input.")



def manage_email_accounts():
	print("Manage email accounts")
	return True



def manage_email_forwarders():
	print("Manage email forwarders")
	return True
