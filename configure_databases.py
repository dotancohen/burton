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
	available_databases = []

	databases = os.popen('sudo mysql --defaults-extra-file=/etc/mysql/debian.cnf --skip-column-names -e "SHOW DATABASES"').read().split('\n')

	for db in databases:
		if db not in default_dbs:
			available_databases.append(db)

	print('\nAvailable databases:')
	for index, value in enumerate(available_databases):
		if value not in default_dbs:
			print(' %s. %s' % (str(index+1), value,))

	new_db_index = index + 1
	print(' %s. Add New Database' % (str(new_db_index+1),))
	print(' 0. Go Back')
	print(' -. Exit')

	while True:

		operation = input(environment.prompt)

		if operation == '0':
			return True
		elif operation == '-':
			sys.exit()
		elif int(operation)-1 == new_db_index:
			add_new_database()
		elif int(operation)-1 < new_db_index:
			manage_database(available_databases[int(operation)-1])
		else:
			print("Invalid input.")

	return True



def add_new_database():
	print("\nAdd new database")
	return True



def manage_database(database):
	print("\nManage database " + database)
	return True



def manage_users():
	print("\nManage users")
	return True



def backup_databases():
	print("\nBackup databases")
	return True
