import pandas as pd
import os, json
from datetime import date
from files import retrieve_files


class scenario(object):

	def __init__(self):
		self.fn = None
		self.result = None

	# fee plan check

	def fee_plan_check(self, resultsfilelocation, today_now, foldername, accountid, customerid,scenario):

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
							if str(data_file_df['AccountID'][i]) == str(accountid) and str(data_file_df['CustomerID'][i]) == str(customerid):
								if data_file_df['PortfolioTransactionId'][i] == 0:
									line1 = {"Test name": "Fee Plan Check", "Result": "Passed", "Output":"For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Fee Plan is present in file {}".format(files1), "Scenario" :str(scenario)}
									break

								else:
									line1 = {"Test name": "Fee Plan Check", "Result": "Failed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Fee Plan is not present in file {}".format(files1),"Scenario" :str(scenario)}

							else:
								line1 = {"Test name": "Fee Plan Check", "Result": "Failed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Fee Plan is not present in file {}".format(files1), "Scenario" :str(scenario)}

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

	def loan_plan_check(self, resultsfilelocation, today_now, foldername, accountid, customerid,scenario):

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

							if str(data_file_df['AccountID'][i]) == str(accountid) and str(data_file_df['CustomerID'][i]) == str(customerid):

								if data_file_df['PortfolioTransactionId'][i] != 0:
									line1 = {"Test name": "Loan Plan Check", "Result": "Passed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Loan Plan is present in file {}".format(files1),"Scenario" :str(scenario)}
									break
								else:
									line1 = {"Test name": "Loan Plan Check", "Result": "Failed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Loan Plan is not present in file {}".format(files1), "Scenario" :str(scenario)}
							else:
								line1 = {"Test name": "Loan Plan Check", "Result": "Failed", "Output":" the Loan Plan is not present in file {}".format(files1),"Scenario" :str(scenario)}

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

	def interest_rate_check(self, resultsfilelocation, today_now, foldername, accountid, customerid, interest_rate, scenario):

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

							if str(data_file_df['AccountID'][i]) == str(accountid) and str(data_file_df['CustomerID'][i]) == str(customerid):

								Monthly_Payment=((data_file_df['OriginalPurchaseAmount'][i]+data_file_df['InterestRate'][i])/12)+data_file_df['OutstandingFees'][i]
								Calculate_interest=((12*Monthly_Payment)-(data_file_df['OriginalPurchaseAmount'][i])-(data_file_df['OutstandingFees'][i]*12))
								IR=round(Calculate_interest,2)*100
								if (str(int(IR)))==str(interest_rate):
									line1 = {"Test name": "Validate InterestRate ", "Result": "Passed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) + " the interest rate is validated in file {}".format(files1), "Scenario" :str(scenario)}
									break
								else:
									line1 = {"Test name": "Validate InterestRate", "Result": "Failed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the interest rate is invalid in file {}".format(files1),"Scenario" :str(scenario)}
							else:
								line1 = {"Test name": "Validate InterestRate", "Result": "Failed",
										 "Output": "For AccountID: " + str(accountid) + " and for CustomerID: " + str(customerid) + " the interest rate is invalid in file {}".format(files1), "Scenario" :str(scenario)}



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

	def term_length_months_check(self, resultsfilelocation, today_now, foldername, accountid, customerid,
								 termlength, scenario ):
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
								if str(data_file_df['TermLengthMonths'][i]) == str(termlength):
									line1 = {"Test name": "Validate TermLengthMonths ", "Result": "Passed",
											 "Output": "For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " the termlengthmonths is validated in file {}".format(files1), "Scenario" :str(scenario)}
									break

								else:
									line1 = {"Test name": "Validate TermLengthMonths", "Result": "Failed",
											 "Output": "For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " the termlengthmonths is invalid in file {}".format(files1),"Scenario" :str(scenario)}
							else:
								line1 = {"Test name": "Validate TermLengthMonths", "Result": "Failed",
										 "Output": "For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " the termlengthmonths is invalid in file {}".format(files1),"Scenario" :str(scenario)}

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

	def validate_original_purchase_amount(self, resultsfilelocation, today_now, foldername, accountid, customerid,originalpurchaseamount,scenario
										  ):
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
													data_file_df['InterestRate'][i]) / 12) +  data_file_df['OutstandingFees'][i]
								Calculate_original_purchase_amount = (
									(12 * Monthly_Payment) - (data_file_df['InterestRate'][i]) - (
										data_file_df['OutstandingFees'][i] * 12))
								if (str(int(Calculate_original_purchase_amount))) == str(originalpurchaseamount):
									line1 = {"Test name": "validate OriginalPurchaseAmount ", "Result": "Passed",
											 "Output": "For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid)  + " the original purchase amount is validated in file {}".format(files1), "Scenario" :str(scenario)}
									break

								else:
									line1 = {"Test name": "validate OriginalPurchaseAmount", "Result": "Failed",
											 "Output": "For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " the original purchase amount is invalid in file {}".format(files1),"Scenario" :str(scenario)}
							else:
								line1 = {"Test name": "validate OriginalPurchaseAmount", "Result": "Failed",
										 "Output": "For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " the original purchase amount is invalid in file {}".format(files1), "Scenario" :str(scenario)}

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
			print("Error encountered:" + str(err))

	# validate RemainingPayments

	def validate_remaining_payment_amounts(self, resultsfilelocation, today_now, foldername, accountid, customerid,
										    remainingpayments,scenario,statementdate):
		try:
			months=11
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
						for i in range(len(data_file_df['AccountID'])):
							if str(data_file_df['AccountID'][i]) == str(accountid) and str(
									data_file_df['CustomerID'][i]) == str(customerid) and str(data_file_df['StatementDate'][i]) == str(statementdate):
									cal_rem_payments = months - data_file_df['ProjectionNumber'][i]
									if cal_rem_payments == remainingpayments:
										line1 = {"Test name": "validate RemainingPayments", "Result": "Passed",
														 "Output": " For AccountID: " + str(
															 accountid) + " and for CustomerID: " + str(
															 customerid) + "The amount {} is validated for file {}".format(str(remainingpayments),str(files1)),"Scenario" :str(scenario)}
										break
									else:
										line1 = {"Test name": "validate RemainingPayments", "Result": "Failed",
												 "Output": " For AccountID: " + str(
													 accountid) + " and for CustomerID: " + str(
													 customerid) + "The amount {} is not validated for file {}".format(str(remainingpayments),str(files1)), "Scenario": str(scenario)}
										break
							else:
								line1 = {"Test name": "validate RemainingPayments", "Result": "Failed",
										 "Output": " For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + "The amount {} is not validated for file {}".format(str(remainingpayments),str(files1)), "Scenario" :str(scenario)}

						break


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
			print("Error encountered ===: " + str(err))

	# validate NextPaymentAmount

	def validate_next_payment_amount(self, resultsfilelocation, today_now, foldername, accountid,
										   customerid,
										   nextpaymentamount,scenario):
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
				Fail = resultsfilelocation + "/" + today_now + "/" + each_feature + "/"

				for root, dirs, files in os.walk("data/" + foldername):
					for file in files:
						files1 = os.path.basename(file)
						full_path = os.path.join(root, files1)
						data_file = pd.read_csv(full_path, sep="|")
						data_file_df = pd.DataFrame(data_file)

						for i in range(len(data_file_df['CustomerID'])):
							if str(data_file_df['AccountID'][i]) == str(accountid) and str(
									data_file_df['CustomerID'][i]) == str(customerid):
									if data_file_df['NextPaymentAmount'][i] ==nextpaymentamount:
										line1 = {"Test name": "validate NextPaymentAmount", "Result": "Passed",
												 "Output": " For AccountID: " + str(
													 accountid) + " and for CustomerID: " + str(
													 customerid)  +"The amount {} is validated for file {}".format(str(nextpaymentamount),str(files1)),"Scenario" :str(scenario)}
										break

									else:
										line1 = {"Test name": "validate NextPaymentAmount", "Result": "Failed",
												 "Output": " For AccountID: " + str(
													 accountid) + " and for CustomerID: " + str(
													 customerid) + " The amount {} is not validated for file {}".format(str(nextpaymentamount),str(files1)),"Scenario" :str(scenario)}

							else:
								line1 = {"Test name": "validate NextPaymentAmount", "Result": "Failed",
										 "Output": " For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " The amount {} is not validated for file {}".format(str(nextpaymentamount),str(files1)), "Scenario" :str(scenario)}


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

	#validate principal applied
	def validate_principal_applied(self, resultsfilelocation, today_now, foldername, accountid, customerid,
										    amountappliedtoloan,scenario):
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
								if str(data_file_df['AmountAppliedToLoan'][i]) == str(amountappliedtoloan) and str(
										amountappliedtoloan) == "10000.0":

									line1 = {"Test name": "validate PrincipalApplied to loan", "Result": "Passed",
											 "Output": " For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " The amount {} is not validated for file {}".format(str(amountappliedtoloan),str(files1)),"Scenario" :str(scenario)}
									break

								else:
									line1 = {"Test name": "validate PrincipalApplied to loan", "Result": "Failed",
											 "Output": " For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
													 customerid)  + " The amount {} is not validated for file {}".format(str(amountappliedtoloan),str(files1)), "Scenario" :str(scenario)}
							else:
								line1 = {"Test name": "validate PrincipalApplied to loan", "Result": "Failed",
										 "Output": " For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + "  the amount of principal applied is not validated "" The amount {} is not validated for file {}".format(str(amountappliedtoloan),str(files1)),"Scenario" :str(scenario)}


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

	#validate monthly fee applied
	def validate_monthly_fee_applied(self, resultsfilelocation, today_now, foldername, accountid, customerid,
										    monthlyfee,scenario):
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
								if str(data_file_df['AmountAppliedToLoan'][i]) == str(monthlyfee) and str(
										monthlyfee) == "14.0":

									line1 = {"Test name": "validate MonthlyFeeApplied to loan", "Result": "Passed",
											 "Output": " For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid)  + " The amount {} is validated for file {}".format(str(monthlyfee),str(files1)), "Scenario" :str(scenario)}
									break

								else:
									line1 = {"Test name": "validate MonthlyFeeApplied to loan", "Result": "Failed",
											 "Output": " For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid)  + " The amount {} is not validated for file {}".format(str(monthlyfee),str(files1)),"Scenario" :str(scenario)}
							else:
								line1 = {"Test name": "validate MonthlyFeeApplied to loan", "Result": "Failed",
										 "Output": " For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " The amount {} is not validated for file {}".format(str(monthlyfee),str(files1)),"Scenario" :str(scenario)}

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

	#validate origination fee applied
	def validate_origination_fee_applied(self, resultsfilelocation, today_now, foldername, accountid, customerid,
										    originationfee,scenario):
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
								if str(data_file_df['AmountAppliedToLoan'][i]) == str(originationfee) and str(
										originationfee) == "100.0":

									line1 = {"Test name": "validate OriginationFeeApplied to loan", "Result": "Passed",
											 "Output": " For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid)  + " The amount {} is validated for file {}".format(str(originationfee),str(files1)), "Scenario" :str(scenario)}
									break

								else:
									line1 = {"Test name": "validate OriginationFeeApplied to loan", "Result": "Failed",
											 "Output": " For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid)  + " The amount {} is not validated for file {}".format(str(originationfee),str(files1)),"Scenario" :str(scenario)}
							else:
								line1 = {"Test name": "validate OriginationFeeApplied to loan", "Result": "Failed",
										 "Output": " For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " The amount {} is not validated for file {}".format(
											 str(originationfee), str(files1)), "Scenario": str(scenario)}

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

	# validate outstanding fees applied
	def validate_outstanding_fees_applied(self, resultsfilelocation, today_now, foldername, accountid, customerid,
										 outstandingfees,scenario):
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
				Fail = resultsfilelocation + "/" + today_now + "/" + each_feature + "/"

				for root, dirs, files in os.walk("data/" + foldername):
					for file in files:
						files1 = os.path.basename(file)
						full_path = os.path.join(root, files1)
						data_file = pd.read_csv(full_path, sep="|")
						data_file_df = pd.DataFrame(data_file)

						for i in range(len(data_file_df['CustomerID'])):
							if str(data_file_df['AccountID'][i]) == str(accountid) and str(
									data_file_df['CustomerID'][i]) == str(customerid):
								if str(data_file_df['OutstandingFees'][i]) == str(outstandingfees):

									line1 = {"Test name": "validate Oustandingfees applied to loan",
											 "Result": "Passed",
											 "Output": " For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " The amount {} is validated for file {}".format(str(outstandingfees),str(files1)),"Scenario" :str(scenario)}
									break

								else:
									line1 = {"Test name": "validate Outstandingfees applied to loan",
											 "Result": "Failed",
											 "Output": " For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " The amount {} is not validated for file {}".format(str(outstandingfees),str(files1)),"Scenario" :str(scenario)}
							else:
								line1 = {"Test name": "validate Outstandingfees applied to loan",
										 "Result": "Failed",
										 "Output": " For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " The amount {} is not validated for file {}".format(str(outstandingfees),str(files1)), "Scenario" :str(scenario)}

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


	# validate current due
	def validate_current_due(self, resultsfilelocation, today_now, foldername, accountid, customerid,
										  currentdue,scenario):
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
				Fail = resultsfilelocation + "/" + today_now + "/" + each_feature + "/"

				for root, dirs, files in os.walk("data/" + foldername):
					for file in files:
						files1 = os.path.basename(file)
						full_path = os.path.join(root, files1)
						data_file = pd.read_csv(full_path, sep="|")
						data_file_df = pd.DataFrame(data_file)

						for i in range(len(data_file_df['CustomerID'])):
							if str(data_file_df['AccountID'][i]) == str(accountid) and str(
									data_file_df['CustomerID'][i]) == str(customerid):

									Cal_current_due = ((data_file_df['OutstandingPrincipal'][i])/12)+(data_file_df['OutstandingFees'][i])+((data_file_df['OutstandingPrincipal'][i])/100)
									if str(data_file_df['CurrentDue'][i]) == Cal_current_due and str(data_file_df['CurrentDue'][i]) == currentdue:

										line1 = {"Test name": "validate CurrentDue of loan",
												 "Result": "Passed",
												 "Output": " For AccountID: " + str(
													 accountid) + " and for CustomerID: " + str(
													 customerid) + " The amount {} is validated for file {}".format(str(currentdue),str(files1)),"Scenario" :str(scenario)}
										break

									else:
										line1 = {"Test name": "validate CurrentDue of loan",
												 "Result": "Failed",
												 "Output": " For AccountID: " + str(
													 accountid) + " and for CustomerID: " + str(
													 customerid) + " The amount {} is not validated for file {}".format(str(currentdue),str(files1)), "Scenario" :str(scenario)}
							else:
								line1 = {"Test name": "validate CurrentDue of loan",
										 "Result": "Failed",
										 "Output": " For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " The amount {} is not validated for file {}".format(str(currentdue),str(files1)),"Scenario" :str(scenario)}

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


	# validate past due
	def validate_past_due(self, resultsfilelocation, today_now, foldername, accountid, customerid,
										  pastdue,scenario):
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
				Fail = resultsfilelocation + "/" + today_now + "/" + each_feature + "/"

				for root, dirs, files in os.walk("data/" + foldername):
					for file in files:
						files1 = os.path.basename(file)
						full_path = os.path.join(root, files1)
						data_file = pd.read_csv(full_path, sep="|")
						data_file_df = pd.DataFrame(data_file)

						for i in range(len(data_file_df['CustomerID'])):
							if str(data_file_df['AccountID'][i]) == str(accountid) and str(
									data_file_df['CustomerID'][i]) == str(customerid):

									if str(data_file_df['PastDue'][i]) == pastdue:

										line1 = {"Test name": "validate PastDue of loan",
												 "Result": "Passed",
												 "Output": " For AccountID: " + str(
													 accountid) + " and for CustomerID: " + str(
													 customerid) + " The amount {} is validated for file {}".format(str(pastdue),str(files1)), "Scenario" :str(scenario)}
										break

									else:
										line1 = {"Test name": "validate PastDue of loan",
												 "Result": "Failed",
												 "Output": " For AccountID: " + str(
													 accountid) + " and for CustomerID: " + str(
													 customerid) + " The amount {} is not validated for file {}".format(str(pastdue),str(files1)),"Scenario" :str(scenario)}
							else:
								line1 = {"Test name": "validate PastDue of loan",
										 "Result": "Failed",
										 "Output": " For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " The amount {} is not validated for file {}".format(str(pastdue),str(files1)),"Scenario" :str(scenario)}

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


	#validate amount applied on cycledate
	def validate_amount_applied_on_cycledate(self, resultsfilelocation, today_now, foldername, accountid, customerid, cycledate,scenario):
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
				Fail = resultsfilelocation + "/" + today_now + "/" + each_feature + "/"
				for root, dirs, files in os.walk("data/" + foldername):

					for file in files:
						files1 = os.path.basename(file)
						full_path = os.path.join(root, files1)
						data_file = pd.read_csv(full_path, sep="|")
						data_file_df = pd.DataFrame(data_file)

						for i in range(len(data_file_df['CustomerID'])):
							if str(data_file_df['AccountID'][i]) == str(accountid) and str(
									data_file_df['CustomerID'][i]) == str(customerid):
								if str(data_file_df['CycleDate'][i]) == cycledate:
									Cal_amount_on_Cycle_Date = data_file_df['PrincipalBalance'][i] + data_file_df['FeeBalance'][i]
									if str(data_file_df['CurrentBalance'][i]) == Cal_amount_on_Cycle_Date:
										line1 = {"Test name": "validate for the amount applied to Cycle Date of loan",
												 "Result": "Passed",
												 "Output": " For AccountID: " + str(
													 accountid) + " and for CustomerID: " + str(
													 customerid) + " The amount applied to cycledate {} is validated for file {}".format(str(cycledate),str(files1)),"Scenario" :str(scenario)}
										break
									else:
										line1 = {"Test name": "validate for the amount applied to Cycle Date of loan",
												 "Result": "Failed",
												 "Output": " For AccountID: " + str(
													 accountid) + " and for CustomerID: " + str(
													 customerid) + " The amount applied to cycledate {} is not validated for file {}".format(str(cycledate),str(files1)),"Scenario" :str(scenario)}
								else:
									line1 = {"Test name": "validate for the amount applied to Cycle Date of loan",
											 "Result": "Failed",
											 "Output": " For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " The amount applied to cycledate {} is not validated for file {}".format(str(cycledate),str(files1)) ,"Scenario" :str(scenario)}
							else:
								line1 = {"Test name": "validate for the amount applied to Cycle Date of loan",
										 "Result": "Failed",
										 "Output": " For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " The amount applied to cycledate {} is not validated for file {}".format(str(cycledate),str(files1)),"Scenario" :str(scenario)}

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


	# validate loan Plans
	def multiple_loan_validation(self, resultsfilelocation, today_now, accountid, customerid,scenario,foldername):

		try:
			feature_list = []
			count = 0
			for subdir, dirs, files in os.walk("features/"):
				for file in files:
					if file.endswith(".feature"):
						base = os.path.basename(file)
						feature_names = os.path.splitext(base)[0]
						feature_list.append(feature_names)
			for each_feature in feature_list:
				Pass = resultsfilelocation + "/" + today_now + "/" + each_feature + "/"
				Fail = resultsfilelocation + "/" + today_now + "/" + each_feature + "/"
				for root, dirs, files in os.walk("data/" + foldername):
					for file in files:
						files1 = os.path.basename(file)
						full_path = os.path.join(root, files1)
						data_file = pd.read_csv(full_path, sep="|")
						data_file_df = pd.DataFrame(data_file)
						for i in range(len(data_file_df['CustomerID'])):
								if str(data_file_df['AccountID'][i]) == str(accountid) and str(
										data_file_df['CustomerID'][i]) == str(customerid):
									print(data_file_df['LoanID'][i])
									if data_file_df['LoanID'].count() > 1:
										count = count + 1
						if count > 1:
							line1 = {"Test name": "Multiple Loan Plan Validation", "Result": "Passed",
									 "Output": "For AccountID: " + str(
										 accountid) + " and for CustomerID: " + str(
										 customerid) + " The multiple loans is validated for file {}".format(
										 str(files1)), "Scenario": str(scenario)}


						else:
							line1 = {"Test name": "Multiple Loan Plan Validation", "Result": "Failed",
									 "Output": "For AccountID: " + str(
										 accountid) + " and for CustomerID: " + str(
										 customerid) + " The multiple loans is validated for file {}".format(
										 str(files1)), "Scenario": str(scenario)}

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


