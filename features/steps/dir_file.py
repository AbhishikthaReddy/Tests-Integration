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
		mydir_feeplan_validation = os.path.join(resultsfilelocation, today_now, "Fee Plan Validation")
		mydir_loanplan_validation = os.path.join(resultsfilelocation, today_now, "Loan Plan Validation")
		mydir_principal_validation = os.path.join(resultsfilelocation, today_now, "Principal Validation")
		mydir_monthlyfee_validation = os.path.join(resultsfilelocation, today_now, "Monthlyfee Validation")
		mydir_originationfee_validation = os.path.join(resultsfilelocation, today_now, "Originationfee Validation")
		if not os.path.exists(today_now + "/" + mydir_feeplan):
			os.makedirs(mydir_feeplan)

		if not os.path.exists(today_now + "/" + mydir_loanplan):
			os.makedirs(mydir_loanplan)

		if not os.path.exists(today_now + "/" + mydir_feeplan_validation):
			os.makedirs(mydir_feeplan_validation)

		if not os.path.exists(today_now + "/" + mydir_loanplan_validation):
			os.makedirs(mydir_loanplan_validation)

		if not os.path.exists(today_now + "/" + mydir_principal_validation):
			os.makedirs(mydir_principal_validation)

		if not os.path.exists(today_now + "/" + mydir_monthlyfee_validation):
			os.makedirs(mydir_monthlyfee_validation)

		if not os.path.exists(today_now + "/" + mydir_originationfee_validation):
			os.makedirs(mydir_originationfee_validation)

		return today_now