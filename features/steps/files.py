import pandas as pd

class retrieve_files(object):
	"""docstring for Count"""

	def __init__(self):
		self.fn = None


	def files(self, date, masterfile_loc):
		try:
			masterfile = pd.read_json(masterfile_loc)
			data_file_loc = masterfile['partner_data']['datafilelocation']
			fieldsep = masterfile['partner_data']['fieldseparator']
			return fieldsep
		except Exception as err:
			print(err)
