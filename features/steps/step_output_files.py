from behave      import *
from hamcrest    import assert_that, equal_to
from transformation import scenario
from files import retrieve_files
from dir_file import dir_create

try:

	@given('AccountId "{accountid}" and CustomerId "{customerid}" and date "{date}"')
	def step_accountid_customerid(context, accountid, customerid, date):

		masterfile_loc = context.config.userdata.get("masterfile_loc")
		context.resultsfiles_loc = context.config.userdata.get("resultsfiles_loc")
		context.date = date
		context.files = retrieve_files()
		context.dir_file = dir_create()
		context.today_now = context.dir_file.dir(context.resultsfiles_loc)
		fieldsep = context.files.files(date, masterfile_loc)
		context.transformation = scenario()
		context.accountid = accountid
		context.customerid = customerid
		pass

	@given('date "{date2}"')
	def step_date(context,date2):
		masterfile_loc = context.config.userdata.get("masterfile_loc")
		context.resultsfiles_loc = context.config.userdata.get("resultsfiles_loc")
		context.date = date2
		context.files = retrieve_files()
		context.dir_file = dir_create()
		context.today_now = context.dir_file.dir(context.resultsfiles_loc)
		fieldsep = context.files.files(date2, masterfile_loc)
		context.transformation = scenario()
		pass

	@when('single loan is booked')
	def step_single_loan_booked(context):
		pass

	@when('multiple loans are booked')
	def step_single_loan_booked(context):
		pass

	@then('check fee plan in "{foldername}"')
	def step_check_fee_plan(context, foldername):
		scenario = context.scenario
		context.transformation.fee_plan_check(context.resultsfiles_loc, context.today_now, foldername, context.accountid, context.customerid, scenario)
		pass

	@then('check loan plan in "{foldername}"')
	def step_check_loan_plan(context, foldername):
		scenario = context.scenario
		context.transformation.loan_plan_check(context.resultsfiles_loc, context.today_now, foldername, context.accountid, context.customerid,scenario)
		pass

	@then('validate InterestRate of "{interest_rate}" in "{foldername}"')
	def step_check_interestrate(context, foldername, interest_rate):
		scenario = context.scenario
		context.transformation.interest_rate_check(context.resultsfiles_loc, context.today_now, foldername,context.accountid, context.customerid, interest_rate,scenario)
		pass

	@then('validate TermLengthMonths of "{term_length_months}" in "{foldername}"')
	def step_check_termlengthmonths(context, foldername, term_length_months):
		scenario = context.scenario
		context.transformation.term_length_months_check(context.resultsfiles_loc, context.today_now, foldername,
												   context.accountid, context.customerid, term_length_months,scenario)
		pass

	@then('validate OriginalPurchaseAmount of "{original_purchase_amount}" in "{foldername}"')
	def step_check_originalpurchaseamount(context, foldername, original_purchase_amount):
		scenario = context.scenario
		context.transformation.validate_original_purchase_amount(context.resultsfiles_loc, context.today_now, foldername,	context.accountid, context.customerid, original_purchase_amount,scenario)
		pass

	@then('validate NextPaymentAmount of "{nextpaymentamount}" in "{foldername}"')
	def step_check_nextpaymentamount(context, foldername, nextpaymentamount):
		scenario = context.scenario
		context.transformation.validate_next_payment_amount(context.resultsfiles_loc, context.today_now, foldername, context.accountid, context.customerid, nextpaymentamount,scenario)
		pass

	@then('validate RemainingPayments of "{remainingpayments}" in "{foldername}" for date "{date1}"')
	def step_check_remainingpayments(context, foldername, remainingpayments,date1):
		scenario = context.scenario
		context.transformation.validate_remaining_payment_amounts(context.resultsfiles_loc, context.today_now,
																 foldername, context.accountid,context.customerid, remainingpayments,scenario,date1)
		pass

	@then('validate Principal applied of "{amountappliedtoloan}" in "{foldername}"')
	def step_check_principal_applied(context, foldername,amountappliedtoloan):
		scenario = context.scenario
		context.transformation.validate_principal_applied(context.resultsfiles_loc, context.today_now,
																 foldername, context.accountid, context.customerid,amountappliedtoloan,scenario)
		pass

	@then('validate monthly fee applied of "{monthlyfee}" in "{foldername}"')
	def step_check_monthly_fee_applied(context, foldername, monthlyfee):
		scenario = context.scenario
		context.transformation.validate_monthly_fee_applied(context.resultsfiles_loc, context.today_now,
														  foldername, context.accountid, context.customerid,
														  monthlyfee,scenario)
		pass

	@then('validate origination fee applied of "{originationfee}" in "{foldername}"')
	def step_check_origination_fee_applied(context, foldername, originationfee):
		scenario = context.scenario
		context.transformation.validate_origination_fee_applied(context.resultsfiles_loc, context.today_now,
														  foldername, context.accountid, context.customerid,
														  originationfee,scenario)
		pass

	@then('validate for the amount applied to Cycle Date "{cycledate}" in "{foldername}"')
	def step_check_amount_applied_cycledate(context, foldername,cycledate):
		scenario = context.scenario
		context.transformation.validate_amount_applied_on_cycledate(context.resultsfiles_loc, context.today_now, foldername, context.accountid, context.customerid,cycledate,scenario)
		pass

	@then('validate OutstandingFees applied of "{outstandingfees}" in "{foldername}"')
	def step_validate_oustandingfees_applied(context, foldername, outstandingfees):
		scenario = context.scenario
		context.transformation.validate_outstanding_fees_applied(context.resultsfiles_loc, context.today_now,
																foldername, context.accountid,context.customerid,outstandingfees,scenario)
		pass

	@then('validate CurrentDue of "{currentdue}" in "{foldername}"')
	def step_validate_currentdue(context, foldername, currentdue):
		scenario = context.scenario
		context.transformation.validate_current_due(context.resultsfiles_loc, context.today_now,
																 foldername, context.accountid, context.customerid,currentdue,scenario)
		pass

	@then('validate PastDue of "{pastdue}" in "{foldername}"')
	def step_validate_currentdue(context, foldername, pastdue):
		scenario = context.scenario
		context.transformation.validate_past_due(context.resultsfiles_loc, context.today_now,
													foldername, context.accountid, context.customerid,
													pastdue,scenario)

		pass

	@then('validate multiple loans in "{foldername}"')
	def step_validate_multiple_loans(context, foldername):
		scenario = context.scenario
		context.transformation.multiple_loan_validation(context.resultsfiles_loc, context.today_now,
														foldername, context.accountid, context.customerid, scenario)
		pass

except Exception as err:
	print("Error encountered "+str(err))
