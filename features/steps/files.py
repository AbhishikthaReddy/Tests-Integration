import pandas as pd, os

class retrieve_files(object):
	"""docstring for Count"""

	def __init__(self):
		self.fn = None


	def files(self, date, masterfile_loc):
		try:
			masterfile = pd.read_json(masterfile_loc)
			data_file_loc = masterfile.datafilelocation.ix[0]
			text_files = masterfile.files
			folder_names = masterfile.files['file1']['filename']
			data_files_all = os.walk(data_file_loc + "/" + folder_names)
			return 
		except Exception as err:
			print(err)
