import os
import sys

# Enable / disable .htaccess for a site
# PHP configuration



environment = ''



def main(env):
	global environment
	environment = env

	while True:
		print("\nConfigure and maintain operating system\n")
		print("Please select an operation:")
		print(" 1. Quick hands-free OS update")
		print(" 2. Run Aptitude package manager")
		#print(" 3. Drop to shell")
		print(" 0. Go Back")
		print(" -. Exit")

		operation = input(environment.prompt)

		if operation == '0':
			return True
		elif operation == '-':
			sys.exit()
		elif operation == '1':
			quick_os_update()
		elif operation == '2':
			run_aptitude()
		else:
			print("Invalid input.")



def quick_os_update():
	print("\nAttempting to perform quick OS update...")

	print("\nUpdating package list:")
	result = os.system("aptitude update")
	print(result)

	print("\nInstalling updated packages:")
	result = os.system("aptitude -y upgrade")
	print(result)

	return True



def run_aptitude():
	print("\nRunning Aptitude...")
	os.system("aptitude")
	return True
