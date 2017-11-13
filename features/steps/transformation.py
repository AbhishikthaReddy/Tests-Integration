import pandas as pd
import os, json
from datetime import date
from files import retrieve_files

class scenario(object):

	def __init__(self):
		self.fn = None

	# fee plan check

	def fee_plan_check(self, resultsfilelocation, today_now, foldername, accountid, customerid, loanid):

		try:
			fee_plan_check_folder = resultsfilelocation + "/" + today_now + "/" + "Fee Plan Check/"
			for root, dirs, files in os.walk("data/"+foldername):
				for file in files:

					files1 = os.path.basename(file)
					full_path = os.path.join(root, files1)

					data_file = pd.read_csv(full_path,sep="|")
					data_file_df = pd.DataFrame(data_file)

					for i in range(len(data_file_df['CustomerID'])):
						if str(data_file_df['AccountID'][i]) == str(accountid) and str(data_file_df['CustomerID'][i]) == str(customerid) and str(data_file_df['LoanID'][i]) == str(loanid):
							if data_file_df['PortfolioTransactionId'][i] == 0:
								line1 = {"Test name": "Fee Plan Check", "Result": "Passed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Fee Plan is present"}
								break

							else:
								line1 = {"Test name": "Fee Plan Check", "Result": "Failed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Fee Plan is not present"}

						else:
							line1 = {"Test name": "Fee Plan Check", "Result": "Failed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Fee Plan is not present"}


					with open(fee_plan_check_folder+"fee_plan_check.json", "a") as output:
						json.dump(line1, output, indent=4)
					output.close()
		except Exception as err:

			print("Error encountered: "+str(err))

	# loan plan check

	def loan_plan_check(self, resultsfilelocation, today_now, foldername, accountid, customerid, loanid):

		try:
			loan_plan_check_folder = resultsfilelocation + "/" + today_now + "/" + "Loan Plan Check/"

			for root, dirs, files in os.walk("data/"+foldername):
				for file in files:
					files1 = os.path.basename(file)
					full_path = os.path.join(root, files1)
					data_file = pd.read_csv(full_path,sep="|")
					data_file_df = pd.DataFrame(data_file)

					for i in range(len(data_file_df['CustomerID'])):

						if str(data_file_df['AccountID'][i]) == str(accountid) and str(data_file_df['CustomerID'][i]) == str(customerid) and str(data_file_df['LoanID'][i]) == str(loanid):

							if data_file_df['PortfolioTransactionId'][i] != 0:
								line1 = {"Test name": "Loan Plan Check", "Result": "Passed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Loan Plan is present"}
								break
							else:
								line1 = {"Test name": "Loan Plan Check", "Result": "Failed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Loan Plan is not present"}
						else:
							line1 = {"Test name": "Loan Plan Check", "Result": "Failed", "Output": "Incorrect Data Provided"}

					with open(loan_plan_check_folder+"loan_plan_check.json", "a") as output:
						json.dump(line1, output, indent=4)
					output.close()
		except Exception as err:
			print("Error encountered: "+str(err))

	def interest_rate_check(self, resultsfilelocation, today_now, foldername, accountid, customerid, loanid):
		try:
			fee_plan_validation_folder = resultsfilelocation + "/" + today_now + "/" + "Fee Plan Validation/"

			for root, dirs, files in os.walk("data/"+foldername):
				for file in files:
					files1 = os.path.basename(file)
					full_path = os.path.join(root, files1)
					data_file = pd.read_csv(full_path,sep="|")
					data_file_df = pd.DataFrame(data_file)

					for i in range(len(data_file_df['CustomerID'])):

						if str(data_file_df['AccountID'][i]) == str(accountid) and str(data_file_df['CustomerID'][i]) == str(customerid) and str(data_file_df['LoanID'][i]) == str(loanid):
							
							if data_file_df['PortfolioTransactionId'][i] == 0:
								Monthly_Payment=((data_file_df['OriginalPurchaseAmount'][i]+data_file_df['InterestRate'][i])/12)+data_file_df['OutstandingFees'][i]
								Calculate_interest=((12*Monthly_Payment)-(data_file_df['OriginalPurchaseAmount'][i])-(data_file_df['OutstandingFees'][i]*12))
								IR=round(Calculate_interest,2)*100
								if (str(int(IR)))==str(interest_rate):
									line1 = {"Test name": "Validate InterestRate ", "Result": "Passed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" and for LoanID :"+str(loanid)+ "the interest rate is validated"}
									break
								else:
									line1 = {"Test name": "Validate InterestRate", "Result": "Failed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the interest rate is invalid"}

					with open(fee_plan_validation_folder+"fee_plan_validation.json", "a") as output:
						json.dump(line1, output, indent=4)
						output.close()

		except Exception as err:
			print("Error encountered: "+str(err))