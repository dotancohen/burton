import os
import sys



environment = ''



def main(env):
	global environment
	environment = env

	while True:
		print("\nConfigure Databases\n")
		print("Please select an operation:")
		print(" 1. Add/Remove database")
		print(" 2. Add/Remove users")
		print(" 3. Backup databases")
		print(" 0. Go Back")
		print(" -. Exit")

		operation = input(environment.prompt)

		if operation == '0':
			return True
		elif operation == '-':
			sys.exit()
		elif operation == '1':
			manage_databases()
		elif operation == '2':
			manage_users()
		elif operation == '3':
			backup_databases()
		else:
			print("Invalid input.")



def manage_databases():

	print("\nManage databases")

	default_dbs = ['information_schema', 'mysql', 'performance_schema', '']

	databases = os.popen('sudo mysql --defaults-extra-file=/etc/mysql/debian.cnf --skip-column-names -e "SHOW DATABASES"').read().split('\n')

	print("\nAvailable databases:")
	for index, value in enumerate(databases):
		if value not in default_dbs:
			print(str(index) + ': ' + value)

	while True:
		print("\nConfigure Databases\n")
		print("Please select an operation:")
		print(" 1. Add/Remove database")
		print(" 2. Add/Remove users")
		print(" 3. Backup databases")
		print(" 0. Go Back")
		print(" -. Exit")

		operation = input(environment.prompt)

		if operation == '0':
			return True
		elif operation == '-':
			sys.exit()
		elif operation == '1':
			manage_databases()
		elif operation == '2':
			manage_users()
		elif operation == '3':
			backup_databases()
		else:
			print("Invalid input.")

	return True



def manage_users():
	print("\nManage users")
	return True



def backup_databases():
	print("\nBackup databases")
	return True
