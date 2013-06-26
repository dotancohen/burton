#!/usr/bin/python3
import platform
import sys


burton_version = '0.1'


def system_statistics():
	print("\nSystem Statistics\n")

	print("Quick Stats:")
	print("CPU:")
	print("Memory:")
	print("Bandwidth:")
	print("Disk Space:")

	print("\nPlease select an operation:")
	print(" 1. Detailed Foo")
	print(" 2. Detailed Bar")

	operation = input(">> ")



def configure_websites():
	print("\nConfigure Websites\n")
	print("Please select an operation:")
	print(" 1. Add a new website")

	operation = input(">> ")



def main(argv):
	global burton_version

	print("\nWelcome to Burton " + burton_version + "!")

	print("\nPlease select an operation:")
	print(" 1. System statistics")
	print(" 2. Configure websites")
	# print(" 3. Configure databases")
	# print(" 4. Configure email")

	operation = input(">> ")

	if operation == '1':
		system_statistics()
	elif operation == '2':
		configure_websites()
	else:
		print("Invalid input! Exiting!")

	sys.exit()



if __name__ == '__main__':
	main(sys.argv)
