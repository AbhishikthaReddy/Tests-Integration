from behave      import *
from hamcrest    import assert_that, equal_to
from transformation import scenario
from files import retrieve_files
from dir_file import dir_create
import pandas as pd

try:
	@given('AccountId "{accountid}" and CustomerId "{customerid}" and LoanId "{loanid}"')
	def step_accountid_customerid_loanid(context, accountid, customerid, loanid):

		masterfile_loc = context.config.userdata.get("masterfile_loc")
		context.resultsfiles_loc = context.config.userdata.get("resultsfiles_loc")
		date = context.config.userdata.get("date")
		context.files = retrieve_files()
		context.dir_file = dir_create()
		context.today_now = context.dir_file.dir(context.resultsfiles_loc)
		fieldsep = context.files.files(date, masterfile_loc)
		context.transformation = scenario()
		context.accountid = accountid
		context.customerid = customerid
		context.loanid = loanid
		pass

	@when('single loan is booked')
	def step_single_loan_booked(context):
		pass

	@then('check fee plan in "{foldername}"')
	def step_check_fee_plan(context, foldername):
		context.transformation.fee_plan_check(context.resultsfiles_loc, context.today_now, foldername, context.accountid, context.customerid, context.loanid)
		pass

	@then('check loan plan in "{foldername}"')
	def step_check_loan_plan(context, foldername):
		context.transformation.loan_plan_check(context.resultsfiles_loc, context.today_now, foldername, context.accountid, context.customerid, context.loanid)
		pass

	@then('check InterestRate in "{foldername}"')
	def step_check_interestrate(context, foldername):
		pass

	@then('check TermLengthMonths in "{foldername}"')
	def step_check_termlengthmonths(context, foldername):
		pass

	@then('check OriginalPurchaseAmount in "{foldername}"')
	def step_check_originalpaymentamount(context, foldername):
		pass

	@then('validate NextPaymentAmount of "{amount}" in "{foldername}"')
	def step_check_nextpaymentamount(context, foldername, amount):
		pass

	@then('validate RemainingPayments of "{amount}" in "{foldername}"')
	def step_check_remaningpayments(context, foldername, amount):
		pass

	@then('check Principal applied in "{foldername}"')
	def step_check_principal_applied(context, foldername):
		pass

	@then('check monthly fee applied in "{foldername}"')
	def step_check_monthly_fee_applied(context, foldername):
		pass

	@then('check origination fee applied in "{foldername}"')
	def step_check_origination_fee_applied(context, foldername):
		pass

	@then('check for the amount applied to Cycle Date "{date}" in "{foldername1}" and "{foldername2}')
	def step_check_amount_applied_cycledate(context, foldername1, foldername2, date):
		pass

	@then('validate OutstandingFees applied of "{fee}" in "{foldername}"')
	def step_validate_oustandingfees_applied(context, foldername, fee):
		pass

	@then('validate CurrentDue of "{due}" in "{foldername}"')
	def step_validate_currentdue(context, foldername, due):
		pass

except Exception as err:
	print("Error encountered "+str(err))