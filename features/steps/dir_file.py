import os
import datetime

class dir_create(object):
	"""docstring for Count"""

	def __init__(self):
		self.fn = None

	def dir(self, resultsfilelocation):

		today_now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
		mydirs = ["SER004", "SER007", "SER008"]
		rootpath = os.path.join(resultsfilelocation, today_now)
		if not os.path.exists(rootpath):
			os.mkdir(rootpath)
		for dir in mydirs:
			if not os.path.exists(os.path.join(rootpath, dir)):
				os.mkdir(os.path.join(rootpath, dir))

		# mydir_SER004 = os.path.join(resultsfilelocation, today_now, "SER004")
        #
        #
		# if not os.path.exists(mydir_SER004):
		# 	os.makedirs(mydir_SER004)

		# if not os.path.exists(mydir_SER004_fail):
		# 	os.makedirs(mydir_SER004_fail)

		# if not os.path.exists(mydir_pass):
		# 	os.makedirs(mydir_pass)
        #
		# if not os.path.exists(mydir_fail):
		# 	os.makedirs(mydir_fail)

		# if not os.path.exists(mydir_loanplan):
		# 	os.makedirs(mydir_loanplan)
        #
		# if not os.path.exists(mydir_feeplan_validation):
		# 	os.makedirs(mydir_feeplan_validation)
        #
		# if not os.path.exists(mydir_loanplan_validation):
		# 	os.makedirs(mydir_loanplan_validation)
        #
		# if not os.path.exists(mydir_principal_validation):
		# 	os.makedirs(mydir_principal_validation)
        #
		# if not os.path.exists(mydir_monthlyfee_validation):
		# 	os.makedirs(mydir_monthlyfee_validation)
        #
		# if not os.path.exists(mydir_originationfee_validation):
		# 	os.makedirs(mydir_originationfee_validation)

		return today_now