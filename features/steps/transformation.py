import pandas as pd
import os, json
from datetime import date
from files import retrieve_files

class scenario(object):

	def __init__(self):
		self.fn = None


	def scenario_writing_to_files(self, termlength, fieldsep, today_now, resultsfilelocation, accountid, customerid, loanid,interest_rate,originalpurchaseamount,remainingpayments):

		try:

			fee_plan_check_folder = resultsfilelocation + "/" + today_now + "/" + "Fee Plan Check/"
			loan_plan_check_folder = resultsfilelocation + "/" + today_now + "/" + "Loan Plan Check/"
			fee_plan_validation_folder = resultsfilelocation + "/" + today_now + "/" + "Fee Plan Validation/"


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
							line1 = {"Test name": "Fee Plan Check", "Result": "Failed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the Fee Plan is not present"}


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


			#fee plan validation--validate interest rate

					for i in range(len(data_file_df['CustomerID'])):

						if str(data_file_df['AccountID'][i]) == str(accountid) and str(data_file_df['CustomerID'][i]) == str(customerid) and str(data_file_df['LoanID'][i]) == str(loanid):
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

			#fee plan validation --- validate termlengthmonths
						for i in range(len(data_file_df['CustomerID'])):

							if str(data_file_df['AccountID'][i]) == str(accountid) and str(data_file_df['CustomerID'][i]) == str(customerid) and str(data_file_df['LoanID'][i]) == str(loanid):
									if str(data_file_df['TermLengthMonths'][i])==str(termlength):
										line1 = {"Test name": "Validate TermLengthMonths ", "Result": "Passed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" and for LoanID :"+str(loanid)+ "the termlengthmonths is validated"}
										break

									else:
										line1 = {"Test name": "Validate TermLengthMonths", "Result": "Failed", "Output": "For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" the termlengthmonths is invalid"}

						with open(fee_plan_validation_folder+"fee_plan_validation.json", "a") as output:
							json.dump(line1, output, indent=4)
							output.close()


			#validate original purchase amount
						for i in range(len(data_file_df['CustomerID'])):

							if str(data_file_df['AccountID'][i]) == str(accountid) and str(
									data_file_df['CustomerID'][i]) == str(customerid) and str(
									data_file_df['LoanID'][i]) == str(loanid):
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
												 customerid) + " and for LoanID :" + str(
												 loanid) + "the interest rate is validated"}
									break

								else:
									line1 = {"Test name": "validate OriginalPurchaseAmount", "Result": "Failed",
											 "Output": "For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " the interest rate is invalid"}

						with open(fee_plan_validation_folder + "fee_plan_validation.json", "a") as output:
							json.dump(line1, output, indent=4)
							output.close()

		except Exception as err:

				print("Error encountered "+str(err))

			#validate nextpayment amount

		#validate NextPayment Amount
		for root, dirs, files in os.walk("data/PortfolioProjectionFile"):

				for file in files:

					files1 = os.path.basename(file)
					full_path = os.path.join(root, files1)

					data_file = pd.read_csv(full_path,sep="|")
					data_file_df = pd.DataFrame(data_file)

					for i in range(len(data_file_df['CustomerID'])):
						if str(data_file_df['AccountID'][i]) == str(accountid) and str(data_file_df['CustomerID'][i]) == str(customerid) and str(data_file_df['LoanID'][i]) == str(loanid):
							if data_file_df['OriginationFee'][i] == 100:
								Cal_nextpayment=data_file_df['Principal'][i]+data_file_df['MonthlyFee'][i]+data_file_df['OriginationFee'][i]
								if data_file_df['Amount'][i] == Cal_nextpayment:
									line1 = {"Test name": "validate NextPaymentAmount", "Result": "Passed", "Output": " For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" and for loanID: "+ str(loanid)+ " the nextpaymentamount is validated " + str(Cal_nextpayment)}
									break

								else:
									line1 = {"Test name": "validate NextPaymentAmount", "Result": "Failed", "Output": " For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid)+" and for loanID: "+ str(loanid) +" the nextpaymentamount is validated " + str(Cal_nextpayment)}


				with open(fee_plan_validation_folder+"fee_plan_validation.json", "a") as output:
					json.dump(line1, output, indent=4)
				output.close()

		#validate remainingpayments
		for root, dirs, files in os.walk("data/PortfolioFile"):

				for file in files:

					files1 = os.path.basename(file)
					full_path = os.path.join(root, files1)

					data_file = pd.read_csv(full_path,sep="|")
					data_file_df = pd.DataFrame(data_file)

					for i in range(len(data_file_df['CustomerID'])):
						if str(data_file_df['AccountID'][i]) == str(accountid) and str(data_file_df['CustomerID'][i]) == str(customerid) and str(data_file_df['LoanID'][i]) == str(loanid):
							monthly_principal=data_file_df['OutstandingPrincipal'][i]/12
							validate_payment=float(remainingpayments)*monthly_principal
							totalpayment_rem=data_file_df['RemainingPayments'][i]*monthly_principal
							if validate_payment == totalpayment_rem:
								line1 = {"Test name": "validate RemainingPayments", "Result": "Passed", "Output": " For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid) +" and for loanID: "+ str(loanid)+ " the remainingpayments is validated for " + str(remainingpayments)}
								break

							else:
								line1 = {"Test name": "validate RemainingPayments", "Result": "Failed", "Output": " For AccountID: "+ str(accountid)+ " and for CustomerID: "+ str(customerid)+" and for loanID: "+ str(loanid) +" the remainingpayments is not validated for " + str(remainingpayments)}


				with open(fee_plan_validation_folder+"fee_plan_validation.json", "a") as output:
					json.dump(line1, output, indent=4)
				output.close()






