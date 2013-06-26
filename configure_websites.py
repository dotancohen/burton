# Enable / disable .htaccess for a site
# PHP configuration


def select_configure_websites():
	while True:
		print("\nConfigure Websites\n")
		print("Please select an operation:")
		print(" 1. Add a new website")

		operation = input(">> ")

		if operation == '0':
			return True
		elif operation == '1':
			add_website()
		else:
			print("Invalid input.")



def add_website():
	print("Add website!")
