import sys

# Uptime
# option to enable cron job to write specific sys stats to a logfile



environment = ''



def main(env):
	global environment
	environment = env

	print("\nSystem Statistics\n")

	print("Quick Stats:")
	print("CPU:")
	print("Memory:")
	print("Bandwidth:")
	print("Disk Space:")

	while True:
		print("\nPlease select an operation:")
		print(" 1. Detailed Foo")
		print(" 2. Detailed Bar")
		print(" 0. Go Back")
		print(" -. Exit")

		operation = input(environment.prompt)

		if operation == '0':
			return True
		elif operation == '-':
			sys.exit()
		elif operation == '1':
			detailed_foo()
		elif operation == '2':
			detailed_bar()
		else:
			print("Invalid input.")



def detailed_foo():
	print("Foo!")
	return True



def detailed_bar():
	print("Bar!")
	return True
