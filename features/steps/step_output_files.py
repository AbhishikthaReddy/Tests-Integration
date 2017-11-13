from behave      import given, when, then
from hamcrest    import assert_that, equal_to
from transformation import scenario
from files import retrieve_files
from dir_file import dir_create
import pandas as pd


@given('the input data')
def step_the_input_data(context):
	
	masterfile_loc = context.config.userdata.get("masterfile_loc")
	date = context.config.userdata.get("date")
	resultsfiles_loc = context.config.userdata.get("resultsfilelocation")
	input_json_data_file = context.config.userdata.get("input_data_file")
	context.files = retrieve_files()
	dir_file = dir_create()
	today_now = dir_file.dir(resultsfiles_loc)
	termlength, fieldsep = context.files.files(date, masterfile_loc)
	

	try:
		input_json_data = pd.read_json(input_json_data_file)


		for i in range(len(input_json_data['Test-cases'])):
			accountid = input_json_data['Test-cases'].ix[i]['AccountID']
			customerid = input_json_data['Test-cases'].ix[i]['CustomerID']
			loanid = input_json_data['Test-cases'].ix[i]['LoanIDs']
			scenarios_to_be_done = input_json_data['Test-cases'].ix[i]['ScenarioOutline']
			interest_rate=input_json_data['Test-cases'].ix[i]['InterestRate']
			originalpurchaseamount=input_json_data['Test-cases'].ix[i]['OriginalPurchaseAmount']
			remainingpayments = input_json_data['Test-cases'].ix[i]['RemainingPayments']
			amountappliedtoloan = input_json_data['Test-cases'].ix[i]['AmountAppliedToLoan']
			# cycledate = input_json_data['Test-cases'].ix[i]['CycleDate']

			if len(scenarios_to_be_done) > 0:

				for i in range(len(scenarios_to_be_done)):

					if scenarios_to_be_done[i] == "3":
						@given('a file for fee plan check')
						def step_given_the_file(context):
							print("Fee Plan check for " + str(input_json_data['Test-cases'].index[i]))
						pass
						@then('validate presence of fee plan')
						def step_presence_of_fee_plan(context):
							context.transformation = scenario()
							context.transformation.scenario_writing_to_files(termlength, fieldsep, today_now, resultsfiles_loc, accountid, customerid, loanid[0],interest_rate,originalpurchaseamount,remainingpayments,amountappliedtoloan)
							pass

					elif scenarios_to_be_done[i] == "4":
						@given('a file for loan plan check')
						def step_given_the_file(context):
							print("Loan Plan check for " + str(input_json_data['Test-cases'].index[i]))
						pass
						@then('validate presence of loan plan')
						def step_presence_of_loan_plan(context):
							pass

					elif scenarios_to_be_done[i] == "5":
						@given('a file for validating fee plan')
						def step_given_the_file(context):
							print("Fee Plan Validation for " + str(input_json_data['Test-cases'].index[i]))
						pass
						@then('validate interest rate for fee plan')
						def step_validate_interest_rate_for_fee_plan(context):
							pass

						@then('validate termlengthmonths for fee plan')
						def step_validate_termlengthmonths_for_fee_plan(context):
							pass

					elif scenarios_to_be_done[i] == "6":
						@given('a file for validating loan plan')
						def step_given_the_file(context):
							print("Loan Plan Validation for " + str(input_json_data['Test-cases'].index[i]))
						pass
						@then('validate interest rate for loan plan')
						def step_validate_interest_rate_for_loan_plan(context):
							pass

						@then('validate termlengthmonths for loan plan')
						def step_validate_termlengthmonths_for_loan_plan(context):
							pass

						@then('validate OriginalPurchaseAmount')
						def step_validate_OriginalPurchaseAmount(context):
							pass

						@then('validate NextPaymentAmount')
						def step_validate_NextPaymentAmount(context):
							pass

						@then('validate RemainingPayments')
						def step_validate_RemainingPayments(context):
							pass
					else:
						print("None of the Scenario is performed")

			else:
				print("Please provide a Scenario for " + str(input_json_data['Test-cases'].index[i]) + " in your Input-Data File")

	except Exception as err:
		print("Error encountered "+str(err))

	pass