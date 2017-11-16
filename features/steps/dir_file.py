import os
import datetime

class dir_create(object):
	"""docstring for Count"""

	def __init__(self):
		self.fn = None

	def dir(self, resultsfilelocation):

		today_now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

		mydirs = []
		for subdir, dirs, files in os.walk("features/"):
			for file in files:
				if file.endswith(".feature"):
					base=os.path.basename(file)
					feature_names = os.path.splitext(base)[0]
					mydirs.append(feature_names)
		rootpath = os.path.join(resultsfilelocation, today_now)
		if not os.path.exists(rootpath):
			os.mkdir(rootpath)
		for dir in mydirs:
			if not os.path.exists(os.path.join(rootpath, dir)):
				os.mkdir(os.path.join(rootpath, dir))


		return today_now