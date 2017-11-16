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
			feature_list = []
			fail_list = []
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
									line1 = {"Test name": "Fee Plan Check", "Result": "Passed", "Output":"For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Fee Plan is present" }
									break

								else:
									fail_list.append("For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Fee Plan is not present")
									line1 = {"Test name": "Fee Plan Check", "Result": "Failed", "Output": str(fail_list)}

							else:
								fail_list.append("For AccountID: " + str(accountid) + " and for CustomerID: " + str(
									customerid) + " the Fee Plan is not present")
								line1 = {"Test name": "Fee Plan Check", "Result": "Failed", "Output": str(fail_list)}

				if line1["Result"] == "Passed":
					filename="PassedFile.json"
					files = os.path.join(Pass,filename)
					with open(files,'a') as f:
						json.dump(line1, f, indent=4)
						f.close()
				else:
					filename = "FailedFile.json"
					files = os.path.join(Fail, filename)
					with open(files, 'a') as f:
						json.dump(line1, f, indent=4)
						f.close()


		except Exception as err:
			print("Error encountered: "+str(err))

	# loan plan check

	def loan_plan_check(self, resultsfilelocation, today_now, foldername, accountid, customerid, loanid):

		try:
			feature_list = []
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

								if data_file_df['PortfolioTransactionId'][i] != 0:
									line1 = {"Test name": "Loan Plan Check", "Result": "Passed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Loan Plan is present"}
									break
								else:
									line1 = {"Test name": "Loan Plan Check", "Result": "Failed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Loan Plan is not present"}
							else:
								line1 = {"Test name": "Loan Plan Check", "Result": "Failed", "Output": "Incorrect Data Provided"}

				if line1["Result"] == "Passed":
					filename="PassedFile.json"
					files = os.path.join(Pass,filename)
					with open(files,'a') as f:
						json.dump(line1, f, indent=4)
						f.close()
				else:
					filename = "FailedFile.json"
					files = os.path.join(Fail, filename)
					with open(files, 'a') as f:
						json.dump(line1, f, indent=4)
						f.close()

		except Exception as err:
			print("Error encountered: "+str(err))


	#validate interest_rate

	def interest_rate_check(self, resultsfilelocation, today_now, foldername, accountid, customerid, loanid, interest_rate):

		try:
			feature_list = []
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
					filename="PassedFile.json"
					files = os.path.join(Pass,filename)
					with open(files,'a') as f:
						json.dump(line1, f, indent=4)
						f.close()
				else:
					filename = "FailedFile.json"
					files = os.path.join(Fail, filename)
					with open(files, 'a') as f:
						json.dump(line1, f, indent=4)
						f.close()

		except Exception as err:
			print("Error encountered: "+str(err))

	# validate termlength months

	def term_length_months_check(self, resultsfilelocation, today_now, foldername, accountid, customerid, loanid,
								 termlength):
		try:
			feature_list = []
			for subdir, dirs, files in os.walk("features/"):
				for file in files:
					if file.endswith(".feature"):
						base = os.path.basename(file)
						feature_names = os.path.splitext(base)[0]
						feature_list.append(feature_names)
			for each_feature in feature_list:
				Pass = resultsfilelocation + "/" + today_now + "/" + each_feature + "/"
				Fail = resultsfilelocation + "/" +today_now  + "/" + each_feature + "/"


				for root, dirs, files in os.walk("data/" + foldername):
					for file in files:
						files1 = os.path.basename(file)
						full_path = os.path.join(root, files1)
						data_file = pd.read_csv(full_path, sep="|")
						data_file_df = pd.DataFrame(data_file)

						for i in range(len(data_file_df['CustomerID'])):

							if str(data_file_df['AccountID'][i]) == str(accountid) and str(
									data_file_df['CustomerID'][i]) == str(customerid) and str(
								data_file_df['LoanID'][i]) == str(loanid):
								if str(data_file_df['TermLengthMonths'][i]) == str(termlength):
									line1 = {"Test name": "Validate TermLengthMonths ", "Result": "Passed",
											 "Output": "For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " and for LoanID :" + str(
												 loanid) + " the termlengthmonths is validated"}
									break

								else:
									line1 = {"Test name": "Validate TermLengthMonths", "Result": "Failed",
											 "Output": "For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " the termlengthmonths is invalid"}
							else:
								line1 = {"Test name": "Validate TermLengthMonths", "Result": "Failed",
										 "Output": "For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " the termlengthmonths is invalid"}

				if line1["Result"] == "Passed":
					filename = "PassedFile.json"
					files = os.path.join(Pass, filename)
					with open(files, 'a') as f:
						json.dump(line1, f, indent=4)
						f.close()
				else:
					filename = "FailedFile.json"
					files = os.path.join(Fail, filename)
					with open(files, 'a') as f:
						json.dump(line1, f, indent=4)
						f.close()
		except Exception as err:
			print("Error encountered: " + str(err))

	# validate originalpurchaseamount

	def validate_original_purchase_amount(self, resultsfilelocation, today_now, foldername, accountid, customerid,
										  originalpurchaseamount):
		try:
			feature_list = []
			for subdir, dirs, files in os.walk("features/"):
				for file in files:
					if file.endswith(".feature"):
						base = os.path.basename(file)
						feature_names = os.path.splitext(base)[0]
						feature_list.append(feature_names)
			for each_feature in feature_list:
				Pass = resultsfilelocation + "/" + today_now + "/" + each_feature + "/"
				Fail = resultsfilelocation + "/" +today_now  + "/" + each_feature + "/"

				for root, dirs, files in os.walk("data/" + foldername):
					for file in files:
						files1 = os.path.basename(file)
						full_path = os.path.join(root, files1)
						data_file = pd.read_csv(full_path, sep="|")
						data_file_df = pd.DataFrame(data_file)

						for i in range(len(data_file_df['CustomerID'])):

							if str(data_file_df['AccountID'][i]) == str(accountid) and str(
									data_file_df['CustomerID'][i]) == str(customerid):
								Monthly_Payment = ((data_file_df['OriginalPurchaseAmount'][i] +
													data_file_df['InterestRate'][i]) / 12) + \
												  data_file_df['OutstandingFees'][i]
								Calculate_original_purchase_amount = (
									(12 * Monthly_Payment) - (data_file_df['InterestRate'][i]) - (
										data_file_df['OutstandingFees'][i] * 12))
								if (str(int(Calculate_original_purchase_amount))) == str(originalpurchaseamount):
									line1 = {"Test name": "validate OriginalPurchaseAmount ", "Result": "Passed",
											 "Output": "For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid)  + " the original purchase amount is validated"}
									break

								else:
									line1 = {"Test name": "validate OriginalPurchaseAmount", "Result": "Failed",
											 "Output": "For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " the original purchase amount is invalid"}
							else:
								line1 = {"Test name": "validate OriginalPurchaseAmount", "Result": "Failed",
										 "Output": "For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " the original purchase amount is invalid"}

				if line1["Result"] == "Passed":
					filename = "PassedFile.json"
					files = os.path.join(Pass, filename)
					with open(files, 'a') as f:
						json.dump(line1, f, indent=4)
						f.close()
				else:
					filename = "FailedFile.json"
					files = os.path.join(Fail, filename)
					with open(files, 'a') as f:
						json.dump(line1, f, indent=4)
						f.close()
		except Exception as err:
			print("Error encountered: " + str(err))

		# validate RemainingPayments

	def validate_remaining_payment_amounts(self, resultsfilelocation, today_now, foldername, accountid, customerid,
										    remainingpayments):
		try:
			feature_list = []
			for subdir, dirs, files in os.walk("features/"):
				for file in files:
					if file.endswith(".feature"):
						base = os.path.basename(file)
						feature_names = os.path.splitext(base)[0]
						feature_list.append(feature_names)
			for each_feature in feature_list:
				Pass = resultsfilelocation + "/" + today_now + "/" + each_feature + "/"
				Fail = resultsfilelocation + "/" +today_now  + "/" + each_feature + "/"


				for root, dirs, files in os.walk("data/" + foldername):
					for file in files:
						files1 = os.path.basename(file)
						full_path = os.path.join(root, files1)
						data_file = pd.read_csv(full_path, sep="|")
						data_file_df = pd.DataFrame(data_file)

						for i in range(len(data_file_df['CustomerID'])):
							if str(data_file_df['AccountID'][i]) == str(accountid) and str(
									data_file_df['CustomerID'][i]) == str(customerid) and str(
								data_file_df['LoanID'][i]) == str(loanid):
								print("kkkkkkkkkkkkk")
								monthly_principal = data_file_df['OutstandingPrincipal'][i] / 12
								validate_payment = float(remainingpayments) * monthly_principal
								totalpayment_rem = data_file_df['RemainingPayments'][i] * monthly_principal
								if validate_payment == totalpayment_rem:
									line1 = {"Test name": "validate RemainingPayments", "Result": "Passed",
											 "Output": " For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " and for loanID: " + str(
												 loanid) + " the remainingpayments is validated for " + str(
												 remainingpayments)}
									break

								else:
									line1 = {"Test name": "validate RemainingPayments", "Result": "Failed",
											 "Output": " For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " and for loanID: " + str(
												 loanid) + " the remainingpayments is not validated for " + str(
												 remainingpayments)}
							else:
								line1 = {"Test name": "validate RemainingPayments", "Result": "Failed",
										 "Output": " For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " and for loanID: " + str(
											 loanid) + " the remainingpayments is not validated for " + str(
											 remainingpayments)}


				if line1["Result"] == "Passed":
					filename = "PassedFile.json"
					files = os.path.join(Pass, filename)
					with open(files, 'a') as f:
						json.dump(line1, f, indent=4)
						f.close()
				else:
					filename = "FailedFile.json"
					files = os.path.join(Fail, filename)
					with open(files, 'a') as f:
						json.dump(line1, f, indent=4)
						f.close()


		except Exception as err:
			print("Error encountered: " + str(err))
