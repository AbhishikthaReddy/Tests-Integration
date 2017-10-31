import os
import datetime

class dir_create(object):
	"""docstring for Count"""

	def __init__(self):
		self.fn = None

	def dir(self, resultsfilelocation):

		today_now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
		mydir_feeplan = os.path.join(resultsfilelocation, today_now, "Fee Plan Check")
		mydir_loanplan = os.path.join(resultsfilelocation, today_now, "Loan Plan Check")

		if not os.path.exists(today_now + "/" + mydir_feeplan):
			os.makedirs(mydir_feeplan)

		if not os.path.exists(today_now + "/" + mydir_loanplan):
			os.makedirs(mydir_loanplan)

		return today_now