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
	result = os.system("sudo service apache2 restart")

	print(result)
	return True



def add_website():

	global environment

	print('\nAdd website.\n')
	input_file = open('./example-files/apache-site', 'r')
	input_file_text = input_file.read()
	input_file.close()

	site_name = input('Website name (without www or http)' + environment.prompt)
	new_filename = '/etc/apache2/sites-available/%s.conf' % (site_name,)
	tmp_filename = '/tmp/%s.conf' % (site_name,)
	# TODO: Check that site_name is legal for both a domain name and a filename.

	while os.path.isfile(new_filename):
		print('Site exists! Please choose another.')
		site_name = input('Website name (without www or http)' + environment.prompt)
		new_filename = '/etc/apache2/sites-available/%s.conf' % (site_name,)
		tmp_filename = '/tmp/%s.conf' % (site_name,)

	new_config = re.sub('SITE', site_name, input_file_text)
	try:
		output_file = open(tmp_filename, 'w')
		output_file.write(new_config)
		output_file.close()
		tmp_move = os.system("sudo mv %s %s" % (tmp_filename, new_filename))
	except PermissionError as e:
		print('\n\nError!')
		print('The current user does not have permission to perform this action.')
		#print('Please run Burton with elevated permissions to resolve this error.\n\n')

	if tmp_move != 0:
		print('\n\nError!')
		print('The current user does not have permission to perform this action.')
		#print('Please run Burton with elevated permissions to resolve this error.\n\n')


	current_user = str(os.getuid())

	result = os.system('sudo mkdir -p /var/www/%s/public_html/' % (site_name,))
	result = os.system('sudo mkdir -p /var/www/%s/logs/' % (site_name,))
	result = os.system('sudo chown -R %s:%s /var/www/%s/' % (current_user, current_user,))
	result = os.system('sudo a2ensite %s.conf' % (site_name,))

	restart_apache()

	return True



def add_ssl():

	global environment

	print("\nAdd SSL to website.\n")
	print("Please enter the URL of the website.\n")
	site_name = input(environment.prompt)
	print("Is this a wildcard certificate? (y/N)\n")
	wildcard = input(environment.prompt)

	if wildcard.lower()=='y':
		print("Generating wildcard cert for *.%s" % (site_name,))
		wildcard = '*.'
	else:
		print("Generating cert for %s" % (site_name,))
		wildcard = ''


	# http://serverfault.com/questions/649990/non-interactive-creation-of-ssl-certificate-requests
	#command_template = 'openssl req -new -newkey rsa:2048 -nodes -sha256 -keyout foobar.com.key -out foobar.com.csr -subj "/C=US/ST=New foobar/L=foobar/O=foobar foobar, Inc./CN=foobar.com/emailAddress=foobar@foobar.com"'

	command_template = "openssl req -new -newkey rsa:2048 -nodes -sha256 -keyout %s.key -out %s.csr -subj \"/CN=%s%s\""

	print(command_template % (site_name, site_name, wildcard, site_name))

	return True

