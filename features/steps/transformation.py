import pandas as pd
import os, json
from datetime import date
from files import retrieve_files


class scenario(object):

	def __init__(self):
		self.fn = None

	# fee plan check

	def fee_plan_check(self, resultsfilelocation, today_now, foldername, accountid, customerid, loanid, feature_name, scenario_name):

		try:
			feature_list = []
			pass_list = []
			fail_list = []
			passedfile =[]
			for subdir, dirs, files in os.walk("features/"):
				for file in files:
					if file.endswith(".feature"):
						base = os.path.basename(file)
						feature_names = os.path.splitext(base)[0]
						feature_list.append(feature_names)
			for each_feature in feature_list:
				Pass = resultsfilelocation + "/" + today_now + "/" + each_feature + "/"
				Fail = resultsfilelocation + "/" +today_now  + "/" + each_feature + "/"
				for root, dirs, files in os.walk("data/"+foldername):
					for file in files:
						files1 = os.path.basename(file)
						full_path = os.path.join(root, files1)
						data_file = pd.read_csv(full_path,sep="|")
						data_file_df = pd.DataFrame(data_file)
						for i in range(len(data_file_df['CustomerID'])):
							if str(data_file_df['AccountID'][i]) == str(accountid) and str(data_file_df['CustomerID'][i]) == str(customerid) and str(data_file_df['LoanID'][i]) == str(loanid):
								if data_file_df['PortfolioTransactionId'][i] == 0:
									line1 = {"Test name": "Fee Plan Check", "Result": "Passed", "Output":"For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Fee Plan is present","location":each_feature }

									break

								else:
									fail_list.append("For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Fee Plan is not present")
									line1 = {"Test name": "Fee Plan Check", "Result": "Failed", "Output": str(fail_list),"location":each_feature }

							else:
								fail_list.append("For AccountID: " + str(accountid) + " and for CustomerID: " + str(
									customerid) + " the Fee Plan is not present")
								line1 = {"Test name": "Fee Plan Check", "Result": "Failed", "Output": str(fail_list),"location":each_feature}

				if line1["Result"] == "Passed":
					filename="PassedFile.json"
					files = os.path.join(Pass,filename)
					with open(files,'w') as f:
						json.dump(line1, f, indent=4)
						f.close()
				else:
					filename = "FailedFile.json"
					files = os.path.join(Fail, filename)
					with open(files, 'w') as f:
						json.dump(line1, f, indent=4)
						f.close()



















				# passedfile.append(Pass)
				# if line1["Result"] == "Passed":
				# 	for i in passedfile:
				# 		print(i)
				# 		with open(i+"passedfile.json", "w") as output:
				# 			print(line1,"000000000000000000")
				# 			output.write(str(line1))
				# 			json.dump(line1, output, indent=4)
				# 			output.close()
					# else:
				# 	with open(Fail+"failed.json", "w+") as output:
				# 		json.dump(line1, output, indent=4)
				# 		output.close()


		except Exception as err:

			print("Error encountered: "+str(err))

	# loan plan check

	def loan_plan_check(self, resultsfilelocation, today_now, foldername, accountid, customerid, loanid):

		try:
			# loan_plan_check_folder = resultsfilelocation + "/" + today_now + "/" + "Loan Plan Check/"
			ser004_pass = resultsfilelocation + "/" + today_now + "/" + "SER004/"
			ser004_fail = resultsfilelocation + "/" + today_now + "/" + "SER004/"

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

			if line1["Result"] == "Passed":

				with open(ser004_pass+"passed_scenarios.json", "a") as output:
					json.dump(line1, output, indent=4)
				output.close()
			else:
				with open(ser004_fail +"failed_senarios.json", "a") as output:
					json.dump(line1, output, indent=4)
				output.close()


		except Exception as err:
			print("Error encountered: "+str(err))

	def interest_rate_check(self, resultsfilelocation, today_now, foldername, accountid, customerid, loanid, interest_rate):
		try:
			ser004_pass = resultsfilelocation + "/" + today_now + "/" + "SER004/"
			ser004_fail = resultsfilelocation + "/" + today_now + "/" + "SER004/"

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
									line1 = {"Test name": "Validate InterestRate ", "Result": "Passed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" and for LoanID :"+str(loanid)+ " the interest rate is validated"}
									break
								else:
									line1 = {"Test name": "Validate InterestRate", "Result": "Failed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the interest rate is invalid"}
							else:
								line1 = {"Test name": "Validate InterestRate", "Result": "Failed",
										 "Output": "For AccountID: " + str(accountid) + " and for CustomerID: " + str(customerid) + " the interest rate is invalid"}
						else:
							line1 = {"Test name": "Validate InterestRate", "Result": "Failed",
									 "Output": "For AccountID: " + str(accountid) + " and for CustomerID: " + str(customerid) + " the interest rate is invalid"}


			if line1["Result"] == "Passed":

				with open(ser004_pass+"passed_scenarios.json", "a") as output:
					json.dump(line1, output, indent=4)
				output.close()
			else:
				with open(ser004_fail +"failed_senarios.json", "a") as output:
					json.dump(line1, output, indent=4)
				output.close()

		except Exception as err:
			print("Error encountered: "+str(err))