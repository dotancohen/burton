import os
import sys

# http://flurdy.com/docs/postfix/
# Note that even with the above tutorial I had problems with sending mail (outgoing)



environment = ''



def main(env):
	global environment
	environment = env

	while True:
		print("\nConfigure Email\n")
		print("Please select an operation:")
		print(" 1. Add email domain")
		print(" 2. Manage email accounts")
		print(" 3. Manage email forwarders")
		print(" 0. Go Back")
		print(" -. Exit")

		operation = input(environment.prompt)

		if operation == '0':
			return True
		elif operation == '-':
			sys.exit()
		elif operation == '1':
			add_email_domain()
		elif operation == '2':
			manage_email_accounts()
		elif operation == '3':
			manage_email_forwarders()
		else:
			print("Invalid input.")



def add_email_domain():

	print("\nAdd email domain")

	# Check that the system has been configured for email services (perhaps store
	# the fact that this has been done in the .burtonrc file)

	# Run relevant SQL queries

	# Generate SPF records

	return True



def manage_email_accounts():
	print("\nManage email accounts")
	return True



def manage_email_forwarders():
	print("\nManage email forwarders")

	# Add a forwarder from a single address to multiple addresses
	# In Plesk this is called a Mail Group

	return True
