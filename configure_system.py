import getpass
import grp
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
		print(" 5. Upload public RSA key to login to remote server")
		print(" 6. Create RSA keys")
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
			upload_public_rsa_key()
		elif operation == '6':
			create_rsa_keys()
		else:
			print("Invalid input.")



def quick_os_update():
	print("\nAttempting to perform quick OS update...")

	print("\nUpdating package list:")
	result = os.system("sudo aptitude update")
	print(result)

	print("\nInstalling updated packages:")
	result = os.system("sudo aptitude -y upgrade")
	print(result)

	return True



def run_aptitude():
	print("\nRunning Aptitude...")
	os.system("sudo aptitude")
	return True



def add_git_repo():

	print('\nAdd Git repo.\n')

	# Hardcoded values
	base_git_dir = '/var/git/'
	git_login_name = 'gituser'


	git_name = input('Git repo name' + environment.prompt)
	# TODO: Validate input

	git_dir = base_git_dir + git_name + '.git'
	user_uid = os.getuid()

	try:
		user_gid = grp.getgrnam(git_login_name).gr_gid
	except KeyError:
		print("The group 'gituser' does not seem to exist. This function is intended to be run on the main Git server only.")
		print("Aborting operation.")
		return False


	os.system("sudo mkdir -p %s" % (git_dir, ))
	os.system("cd %s ; sudo git init --bare --shared" % (git_dir, ))
	os.system("sudo chown -R %s:%s %s" % (user_uid, user_gid, git_dir, ))
	os.system("chmod -R 775 %s" % (git_dir, ))
	os.system("sudo chmod -R -s %s" % (git_dir, ))

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
		print('Aborting operation.')
		return False

	external_command = "cd %s ; " % (dir_name, )
	external_command+= " git status 2>&1 "

	git_check = os.popen(external_command).read().strip()

	if not 'Not a git repository' in git_check:
		print('The specified directory is already in a Git repository: %s' % (dir_name, ))
		print('Aborting operation.')
		return False

	external_command = " find %s -name '.git' -type d " % (dir_name, )
	subdirectory_git = os.popen(external_command).read().strip().split('\n')
	subdirectory_git = [x for x in subdirectory_git if x!='']

	if len(subdirectory_git)>0:
		print("Git directories were found in the following subdirectories:")
		for dirname in subdirectory_git:
			print(" * %s" % (dirname, ))

		continue_install = input("Continue? [y/N]" + environment.prompt).lower()

		if not continue_install=='y' and not continue_install=='yes':
			print('Aborting operation.')
			return False

	git_version = os.popen("git --version | awk '{print $3}'").read().strip().split('.')

	if git_version[0]=='1' and git_version[1]=='9':
		push_default = " git config push.default simple ; "
	else:
		push_default = ''

	external_command = "cd %s ; " % (dir_name, )
	external_command+= " git init ; "
	external_command+= " git config user.name 'Do not work on the server' ; "
	external_command+= " git config user.email 'do_not_work@on.the.server' ; "
	external_command+= push_default
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

	# TODO: Check that the steps completed properly.

	print('Done! If connecting to A NEW PUBLIC REPO then you must do an initial branch-configuration push. Would you like to do that now?')
	initial_push = input('[y/N]' + environment.prompt).lower()

	if initial_push=='y' or initial_push=='yes':
		external_command = " cd %s ; " % (dir_name, )
		external_command+= " git push -u origin master "
		os.system(external_command)

	return True



def upload_public_rsa_key():

	print('\nUpload public RSA key to login to remote server.\n')

	key_path = input('Path to public key' + environment.prompt)
	server = input('server' + environment.prompt)

	if not os.path.exists(key_path):
		print("Key not found: %s" % (key_path, ))
		return False

	external_command = " file %s " % (key_path)
	key_type = os.popen(external_command).read().strip()

	if not 'public key' in key_type:
		print("Does not appear to be a public key! Not continuing!")
		return False

	external_command = " cat %s | ssh %s 'cat >> ~/.ssh/authorized_keys'" % (key_name, server)
	os.popen(external_command).read().strip()

	print("Please SSH into server to verify that the key was uploaded properly")

	return True



def create_rsa_keys():

	print('\nCreate RSA keys.\n')

	key_name = input('Key name [gituser]' + environment.prompt)
	key_directory = input('Where to place the keys [~/.ssh]' + environment.prompt)
	key_password1 = getpass.getpass('Key password' + environment.prompt)
	key_password2 = getpass.getpass('Verify Key password' + environment.prompt)

	if key_password1 != key_password2:
		print('Passwords do not match')
		return False

	if "'" in key_password1:
		print('Quotes in passwords are not yet supported.')
		return False

	if key_name=='':
		key_name = 'rsa_gituser'

	if key_directory=='':
		key_directory = os.path.expanduser('~') + '/.ssh'

	if not key_directory[-1] == '/':
		key_directory+= '/'

	key_directory = os.path.expanduser(key_directory)

	if not os.path.isdir(key_directory):
		print('The specified directory does not seem to exist: %s' % (key_directory, ))
		return False

	key_path = key_directory + key_name

	if os.path.exists(key_path):
		print('Key already exists: %s' % (key_path, ))
		return False

	external_command = " ssh-keygen -f %s -t rsa -P '%s' ; " % (key_path, key_password1, )
	external_command+= " chmod 600 %s*" % (key_path, )

	os.popen(external_command).read().strip()

	if not os.path.exists(key_path):
		print("Could not create key: %s" % (key_path, ))
		return False

	if not os.path.exists(key_path+'.pub'):
		print("Could not create public key: %s.pub" % (key_path, ))
		return False

	print("Keys created:")
	print(key_path)
	print(key_path + '.pub')

	return True

