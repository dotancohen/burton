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
		print(" 3. Add Git public repository")
		print(" 4. Connect directory to remote Git repository")
		print(" 5. Add public RSA key to allow remote logins")
		print(" 6. Add private RSA key to login to remote server")
		print(" 7. Create RSA keys")
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
		elif operation == '3':
			add_git_repo()
		elif operation == '4':
			add_dir_to_git()
		elif operation == '5':
			add_public_rsa_key()
		elif operation == '6':
			add_private_rsa_key()
		elif operation == '7':
			create_rsa_keys()
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



def add_git_repo():

	print('\nAdd Git repo.\n')

	# Hardcoded values
	base_git_dir = '/var/git/'
	git_login_name = 'gituser'


	git_name = input('Git repo name' + environment.prompt)
	# TODO: Validate input

	git_dir = base_git_dir + git_name + '.git'

	os.system("mkdir -p %s" % (git_dir, ))
	os.system("cd %s ; git init --bare --shared" % (git_dir, ))
	os.system("chgrp -R %s %s" % (git_login_name, git_dir, ))

	git_dir_remote = 'ssh://%s%s' % (git_login_name, git_dir, )

	print("The local path to the new Git repository is: %s" % (git_dir, ))
	print("The remote path to the new Git repository is: %s" % (git_dir_remote, ))

	return True



def add_dir_to_git():

	print('\nAdd Git repo.\n')

	dir_name = input('Directory path to add' + environment.prompt)
	git_name = input('Git repo path' + environment.prompt)
	# TODO: Validate input

	if not dir_name.endswith('/'):
		dir_name += '/'

	if not os.path.isdir(dir_name):
		print('The specified directory does not seem to exist: %s' % (dir_name, ))
		return False

	external_command = "cd %s ; " % (dir_name, )
	external_command+= " git status 2>&1 "

	git_check = os.popen(external_command).read().strip()

	if not 'Not a git repository' in git_check:
		print('The specified directory is already in a Git repository: %s' % (dir_name, ))
		return False

	external_command = "cd %s ; " % (dir_name, )
	external_command+= " git init ; "
	external_command+= " git config user.name 'Do not work on the server' ; "
	external_command+= " git config user.email 'do_not_work@on.the.server' ; "
	external_command+= " git add . ; "
	external_command+= " git commit -am 'Initial commit' 2>&1 "

	create_repo = os.popen(external_command).read().strip()

	#TODO: Check!

	git_config_file = dir_name + '.git/config'
	git_config = open(git_config_file, 'a')

	git_append = """
[remote "origin"]
        fetch = +refs/heads/*:refs/remotes/origin/*
        url = %s
[branch "master"]
        remote = origin
        merge = refs/heads/master
""" % (git_name, )

	git_config.write(git_append)

	print('Done! You may need to run the following command to push to the repo:\n    git push origin master')

	return True



def add_public_rsa_key():

	print('\nAdd public RSA key to allow remote logins.\n')

	return True



def add_private_rsa_key():

	print('\nAdd private RSA key to login to remote server.\n')

	return True



def create_rsa_keys():

	print('\nCreate RSA keys.\n')

	return True

