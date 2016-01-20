import configparser
import os



settings_file = None


class Burton(object):


	def __init__(self):

		self.settings_file = self.get_settings_file()

		self.load_default_configuration_profile()

		#config = configparser.ConfigParser()



	def get_settings_file(self):

		config_dir = os.path.realpath(os.path.expanduser('~/.burton'))

		if not os.path.isdir(config_dir):
			print("Creating settings directory: %s ... " % (config_dir,), end='')
			os.mkdir(config_dir)
			if not os.path.isdir(config_dir):
				raise Exception("Cannot create settings direcroty!")
			print("Done!")

		config_file = os.path.join(config_dir, 'burtonrc')

		if os.path.isfile(config_file):
			fh = open(config_file, 'w')
		else:
			print("Creating settings file: %s ... " % (config_file,), end='')
			fh = open(config_file, 'w')
			open(config_file, 'w')
			fh.write('')
			fh.flush()
			if not os.path.isfile(config_file):
				raise Exception("Cannot create settings file!")
			print("Done!")

		return fh



	def load_server_configuration(self, env):
		# Load from config file, set properties as in load_default_configuration_profile()
		print("Not yet implemented!")

		return True



	def load_default_configuration_profile(self):

		self.profile_name = 'default'
		self.prompt = '>> '

		self.host = 'localhost'
		self.username = None
		self.password = None

		example_file_dir = os.path.join(os.getcwd(), 'example-files')
		if not os.path.isdir(example_file_dir):
			print("Creating example files directory: %s ... " % (example_file_dir,), end='')
			os.mkdir(example_file_dir)
			if not os.path.isdir(example_file_dir):
				raise Exception("Cannot create example files direcroty!")
			print("Done!")

		self.example_file_dir =  example_file_dir

		return True

