import pandas as pd
import os, json
from datetime import date
from files import retrieve_files

class scenario(object):

	def __init__(self):
		self.fn = None


	def scenario_writing_to_files(self, termlength, fieldsep, masterfile_loc, today_now, resultsfilelocation, input_json_data_file):

		try:

			input_json_data = pd.read_json(input_json_data_file)
			input_json_data = input_json_data.transpose()
			for i in range(len(input_json_data)):
				accountid = input_json_data.ix[i]['AccountID']
				customerid = input_json_data.ix[i]['CustomerID']
				loanid = input_json_data.ix[i]['LoanID']

				# reading the timestamp folder and the folders in that

				fee_plan_check_folder = resultsfilelocation + "/" + today_now + "/" + "Fee Plan Check/"
				loan_plan_check_folder = resultsfilelocation + "/" + today_now + "/" + "Loan Plan Check/"

				# fee plan check

				for root, dirs, files in os.walk("data/PortfolioFile"):

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
								line1 = {"Test name": "Fee Plan Check", "Result": "Failed", "Output": "Incorrect Data Provided"}

						with open(fee_plan_check_folder+"fee_plan_check.json", "a") as output:
							json.dump(line1, output, indent=4)
						output.close()


				# loan plan check

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

			print("Error encountered "+str(err))
