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

	# validate multiple loan plans

	def multiple_loan_validation(self, resultsfilelocation, today_now, foldername, accountid, customerid):
		try:
			multiple_loan_plan_check_folder = resultsfilelocation + "/" + today_now + "/" + "Multiple Loan Plan Check/"
			print("heloo============================")
			for root, dirs, files in os.walk("data/" + foldername):
				for file in files:
					files1 = os.path.basename(file)
					full_path = os.path.join(root, files1)
					data_file = pd.read_csv(full_path, sep="|")
					data_file_df = pd.DataFrame(data_file)
					count=0
					for i in range(len(data_file_df['CustomerID'])):

						if str(data_file_df['AccountID'][i]) == str(accountid) and str(data_file_df['CustomerID'][i]) == str(customerid):
							count=count+1

							if count > 1:
								line1 = {"Test name": "Multiple Loan Plan Validation", "Result": "Passed",
										 "Output": "For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " , {} loans are present".format(count)}
								break
							else:
								line1 = {"Test name": "Multiple Loan Plan Validation", "Result": "Failed",
										 "Output": "For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " , {} loans are present".format(count)}

					with open(multiple_loan_plan_check_folder + "multiple_loan_plan_check.json", "a") as output:
						json.dump(line1, output, indent=4)
					output.close()

		except Exception as err:
			print("Error encountered: "+str(err))

	# validate interest rate
	def interest_rate_check(self, resultsfilelocation, today_now, foldername, accountid, customerid, loanid, interest_rate):
		try:
			interest_rate_validation_folder = resultsfilelocation + "/" + today_now + "/" + "InterestRate Validation/"

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

							if data_file_df['PortfolioTransactionId'][i] == 0:
								Monthly_Payment = ((data_file_df['OriginalPurchaseAmount'][i] +
													data_file_df['InterestRate'][i]) / 12) + \
												  data_file_df['OutstandingFees'][i]
								Calculate_interest = (
								(12 * Monthly_Payment) - (data_file_df['OriginalPurchaseAmount'][i]) - (
								data_file_df['OutstandingFees'][i] * 12))
								IR = round(Calculate_interest, 2) * 100
								if (str(int(IR))) == str(interest_rate):
									line1 = {"Test name": "Validate InterestRate ", "Result": "Passed",
											 "Output": "For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " and for LoanID :" + str(
												 loanid) + " the interest rate is validated"}
									break
								else:
									line1 = {"Test name": "Validate InterestRate", "Result": "Failed",
											 "Output": "For AccountID: " + str(
												 accountid) + " and for CustomerID: " + str(
												 customerid) + " the interest rate is invalid"}

					with open(interest_rate_validation_folder + "interest_rate_validation.json", "a") as output:
						json.dump(line1, output, indent=4)
						output.close()

		except Exception as err:
			print("Error encountered: " + str(err))

	# validate termlength months

	def term_length_months_check(self, resultsfilelocation, today_now, foldername, accountid, customerid, loanid, termlength):
		try:
			term_length_validation_folder = resultsfilelocation + "/" + today_now + "/" + "TermLengthMonths Validation/"

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
										 "Output": "For AccountID: " + str(accountid) + " and for CustomerID: " + str(
											 customerid) + " and for LoanID :" + str(
											 loanid) + " the termlengthmonths is validated"}
								break

							else:
								line1 = {"Test name": "Validate TermLengthMonths", "Result": "Failed",
										 "Output": "For AccountID: " + str(accountid) + " and for CustomerID: " + str(
											 customerid) + " the termlengthmonths is invalid"}

					with open(term_length_validation_folder + "term_length_months_validation.json", "a") as output:
						json.dump(line1, output, indent=4)
						output.close()

		except Exception as err:
			print("Error encountered: " + str(err))

	#validate originalpurchaseamount

	def validate_original_purchase_amount(self, resultsfilelocation, today_now, foldername, accountid, customerid, loanid, originalpurchaseamount):
		try:
			original_purchase_amount_validation_folder = resultsfilelocation + "/" + today_now + "/" + "OriginalPurchaseAmount Validation/"

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
											 loanid) + " the original purchase amount is validated"}
								break

							else:
								line1 = {"Test name": "validate OriginalPurchaseAmount", "Result": "Failed",
										 "Output": "For AccountID: " + str(
											 accountid) + " and for CustomerID: " + str(
											 customerid) + " the original purchase amount is invalid"}

					with open(original_purchase_amount_validation_folder + "original_purchase_amount_validation.json", "a") as output:
						json.dump(line1, output, indent=4)
						output.close()

		except Exception as err:
			print("Error encountered: " + str(err))

	#validate NextPayment Amount

	# def validate_nextpayment_amount(self, resultsfilelocation, today_now, foldername, accountid, customerid, loanid, nextpaymentamount):
	# 	try:
	# 		line1 = {}
	# 		next_payment_amount_validation_folder = resultsfilelocation + "/" + today_now + "/" + "NextPaymentAmount Validation/"
    #
	# 		for root, dirs, files in os.walk("data/" + foldername):
	# 			for file in files:
	# 				files1 = os.path.basename(file)
	# 				full_path = os.path.join(root, files1)
	# 				data_file = pd.read_csv(full_path, sep="|")
	# 				data_file_df = pd.DataFrame(data_file)
    #
	# 				for i in range(len(data_file_df['CustomerID'])):
	# 					if str(data_file_df['AccountID'][i]) == str(accountid) and str(
	# 							data_file_df['CustomerID'][i]) == str(customerid) and str(
	# 							data_file_df['LoanID'][i]) == str(loanid):
	# 						if data_file_df['OriginationFee'][i] == 0:
	# 							Cal_nextpayment = data_file_df['Principal'][i] + data_file_df['MonthlyFee'][i] + data_file_df['OriginationFee'][i]
	# 							print(Cal_nextpayment,"------------",nextpaymentamount)
	# 							if Cal_nextpayment == nextpaymentamount:
	# 								line1 = {"Test name": "validate NextPaymentAmount", "Result": "Passed",
	# 										 "Output": " For AccountID: " + str(
	# 											 accountid) + " and for CustomerID: " + str(
	# 											 customerid) + " and for loanID: " + str(
	# 											 loanid) + " the nextpaymentamount is validated for amount" + str(
	# 											 nextpaymentamount)}
	# 								break
    #
	# 							else:
	# 								line1 = {"Test name": "validate NextPaymentAmount", "Result": "Failed",
	# 										 "Output": " For AccountID: " + str(
	# 											 accountid) + " and for CustomerID: " + str(
	# 											 customerid) + " and for loanID: " + str(
	# 											 loanid) + " the nextpaymentamount is not validated for amount" + str(
	# 											 nextpaymentamount)}
	# 						else:
	# 							line1 = {"Test name": "validate NextPaymentAmount", "Result": "Failed",
	# 									 "Output": " For AccountID: " + str(
	# 										 accountid) + " and for CustomerID: " + str(
	# 										 customerid) + " and for loanID: " + str(
	# 										 loanid) + " the nextpaymentamount is not validated for amount " + str(
	# 										 nextpaymentamount)}
    #
    #
	# 				with open(next_payment_amount_validation_folder + "next_payment_amount_validation.json", "a") as output:
	# 					json.dump(line1, output, indent=4)
	# 				output.close()
    #
    #
	# 	except Exception as err:
	# 		print("Error encountered: " + str(err))

	#validate RemainingPayments

	def validate_remaining_payment_amounts(self, resultsfilelocation, today_now, foldername, accountid, customerid, loanid, remainingpayments):
		try:
			remainingpayments_validation_folder = resultsfilelocation + "/" + today_now + "/" + "RemainingPayment Validation/"

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
										 "Output": " For AccountID: " + str(accountid) + " and for CustomerID: " + str(
											 customerid) + " and for loanID: " + str(
											 loanid) + " the remainingpayments is validated for " + str(
											 remainingpayments)}
								break

							else:
								line1 = {"Test name": "validate RemainingPayments", "Result": "Failed",
										 "Output": " For AccountID: " + str(accountid) + " and for CustomerID: " + str(
											 customerid) + " and for loanID: " + str(
											 loanid) + " the remainingpayments is not validated for " + str(
											 remainingpayments)}

					with open(remainingpayments_validation_folder + "remaining_payment_validation.json", "a") as output:
						json.dump(line1, output, indent=4)
					output.close()

		except Exception as err:
			print("Error encountered: " + str(err))









