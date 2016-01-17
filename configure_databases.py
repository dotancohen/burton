can_use = True

import os
import sys

try:
	import pymysql
except ImportError:
	can_use = False
	print("Cannot use database component! Please install the pymysql module!")


environment = ''



def main(env):
	global environment, can_use
	environment = env

	if can_use == False:
		print("Cannot use database component! Please install the pymysql module!")
		return False

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



def manage_databases():

	print("\nManage databases")

	default_dbs = ['information_schema', 'mysql', 'performance_schema', '']
	available_databases = []

	databases = os.popen('sudo mysql --defaults-extra-file=/etc/mysql/debian.cnf --skip-column-names -e "SHOW DATABASES"').read().split('\n')

	for db in databases:
		if db not in default_dbs:
			available_databases.append(db)

	print('\nAvailable databases:')
	index = 0
	for index, value in enumerate(available_databases):
		if value not in default_dbs:
			print(' %s. %s' % (str(index+1), value,))

	new_db_index = index + 1
	print(' %s. Create New Database' % (str(new_db_index+1),))
	print(' 0. Go Back')
	print(' -. Exit')

	while True:

		operation = input(environment.prompt)

		if operation == '0':
			return True
		elif operation == '-':
			sys.exit()
		elif int(operation)-1 == new_db_index:
			create_new_database()
		elif int(operation)-1 < new_db_index:
			manage_database(available_databases[int(operation)-1])
		else:
			print("Invalid input.")

	return True



def create_new_database():
	print("\nCreate new database")

	print("\nPlease enter a new database name:")
	db_name = input(environment.prompt)

	db = os.popen('sudo mysql --defaults-extra-file=/etc/mysql/debian.cnf --skip-column-names -e "CREATE DATABASE '+db_name+'"').read().split('\n')

	# Need to check if database was in fact successfully created.
	print("\nDatabase created!\n")

	return True



def manage_database(database):
	print("\nManage database " + database)
	return True



def manage_users():
	print("\nManage users")

	"""
	mysql> SHOW GRANTS FOR someUser;
	Due to a bug in MySQL, GRANT ALL does not permit GRANT FILE.
	Due to a bug in MySQL, GRANT FILE only works with the db.table definition *.* (i.e. globally).
	"""
	return True



def create_new_user(username, db_name):

	print("\nCreate new database user")

	"""
	All privileges:
	mysql> GRANT ALL PRIVILEGES ON someDB.* TO 'userName'@'localhost' IDENTIFIED BY 'passWord' WITH GRANT OPTION;

	Limited:
	mysql> GRANT SELECT, EXECUTE ON someDb.* TO 'userName'@'localhost' IDENTIFIED BY 'passWord';

	mysql> FLUSH PRIVILEGES;
	"""
	return username



def get_users(username=None):

	return True



def backup_databases():
	print("\nBackup databases")
	return True
