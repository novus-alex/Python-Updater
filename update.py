# Python-Updater

import requests
import shutil
import os

__author__ = 'alex'

class Update(object):
	def __init__(self, old_file=str, url=str):
		self.old_file = old_file
		self.url = url
		self.temp_file = 'temp_dir/' + old_file
		self.path = os.path.abspath(old_file).replace(old_file, '')

	def get_new_file(self):
		update_file = requests.get(self.url)
		
		if not os.path.exists(os.path.abspath('temp_dir')):
			os.mkdir('temp_dir')

		open(self.temp_file, 'wb').write(update_file.content)

	def update_file(self):
		if os.path.exists(os.path.abspath(self.old_file)):
			os.remove(os.path.abspath(self.old_file))
		else:
			pass

		shutil.move(self.temp_file, self.path)
		os.rmdir('temp_dir')
