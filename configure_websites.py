import os
import re
import sys

"""
* Perform initial configuration to ensure that the server is set up to work with Burton's format
    sudo chown -R ubuntu:ubuntu /var/www
    mkdir -p /var/www/default/public_html
    mv /var/www/html/index.html /var/www/default/public_html # Ubuntu >=14.04
    mv /var/www/index.html /var/www/default/public_html # Ubuntu <14.04
    rm -rf /var/www/html
    sudo vim /etc/apache2/sites-available/000-default.conf # Ubuntu >=14.04
    sudo vim /etc/apache2/sites-available/default # Ubuntu <14.04
    sudo a2enmod ssl
    sudo service apache2 restart


* Enable / disable .htaccess for a site

* PHP configuration

"""



environment = ''



def main(env):
	global environment
	environment = env

	while True:
		print("\nConfigure Websites\n")
		print("Please select an operation:")
		print(" 1. Restart Apache")
		print(" 2. Add a new website")
		print(" 3. Add SSL to website")
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
		elif operation == '3':
			add_ssl()
		else:
			print("Invalid input.")



def restart_apache():
	print("\nAttempting to restart Apache:")

	# TODO: Print an error when the user does not have permissions to perform the action.
	result = os.system("service apache2 restart")

	print(result)
	return True



def add_website():

	global environment

	print("\nAdd website.\n")
	input_file = open('./example-files/apache-site', 'r')
	input_file_text = input_file.read()
	input_file.close()

	site_name = input("Website name (without www or http)" + environment.prompt)
	new_filename = '/etc/apache2/sites-available/' + site_name + '.conf'
	# TODO: Check that site_name is legal for both a domain name and a filename.

	while os.path.isfile(new_filename):
		print("Site exists! Please choose another.")
		site_name = input("Website name (without www or http)" + environment.prompt)
		new_filename = '/etc/apache2/sites-available/' + site_name + '.conf'

	new_config = re.sub('SITE', site_name, input_file_text)
	try:
		output_file = open(new_filename, 'w')
		output_file.write(new_config)
		output_file.close()
	except PermissionError as e:
		print('\n\nError!')
		print('The current user does not have permission to perform this action.')
		print('Please run Burton with elevated permissions to resolve this error.\n\n')

	# TODO: Print an error when the user does not have permissions to perform the action.
	result = os.system("mkdir -p /var/www/" + site_name + '/public_html/')
	result = os.system("a2ensite " + site_name + '.conf')

	restart_apache()

	return True



def add_ssl():
	print("Add SSL to website!")
	return True
