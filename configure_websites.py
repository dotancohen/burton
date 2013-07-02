import os
import sys

# Enable / disable .htaccess for a site
# PHP configuration



environment = ''



def main(env):
	global environment
	environment = env

	while True:
		print("\nConfigure Websites\n")
		print("Please select an operation:")
		print(" 1. Restart Apache")
		print(" 2. Add a new website")
		print(" 0. Go Back")
		print(" -. Exit")

		operation = input(environment.prompt)

		if operation == '0':
			return True
		elif operation == '-':
			sys.exit()
		elif operation == '1':
			restart_apache()
		elif operation == '2':
			add_website()
		else:
			print("Invalid input.")



def restart_apache():
	print("\nAttempting to restart Apache:")
	result = os.system("service apache2 restart")
	print(result)
	return True



def add_website():
	print("Add website!")
