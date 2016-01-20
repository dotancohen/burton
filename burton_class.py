import configparser
import os



settings_file = None


class Burton(object):


	def __init__(self):


		self.settings_file = self.get_settings_file()

		#config = configparser.ConfigParser()

		self.environment = ''
		self.foo = 'FOOBAR'



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



	def get_settings_default(self):
		# Not yet used

		settings = {
			'example-files': 'example-files-DEFAULT'
		}

		return settings



	def get_user_setting(self, key):
		# Not yet used
		return value

