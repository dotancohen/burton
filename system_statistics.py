def select_system_statistics():
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

		operation = input(">> ")

		if operation == '0':
			return True
		elif operation == '1':
			detailed_foo()
		elif operation == '2':
			detailed_bar()
		else:
			print("Invalid input.")



def detailed_foo():
	print("Foo!")



def detailed_bar():
	print("Bar!")
