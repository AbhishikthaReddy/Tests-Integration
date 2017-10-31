from behave      import given, when, then
from hamcrest    import assert_that, equal_to
from transformation import scenario
from files import retrieve_files


@given('a file')
def step_given_the_file(context):
	context.transformation = scenario()
	context.files = retrieve_files()
	accountid = context.config.userdata.get("accountid")
	customerid = context.config.userdata.get("customerid")
	loanid = context.config.userdata.get("loanid")
	originalpurchaseamount = context.config.userdata.get("originalpurchaseamount")
	disbursementdate = context.config.userdata.get("disbursementdate")
	masterfile_loc = context.config.userdata.get("masterfile_loc")
	date = context.config.userdata.get("date")
	context.files.files(date, masterfile_loc)
	context.transformation.scenario_writing_to_files(accountid, customerid, loanid, originalpurchaseamount, disbursementdate, masterfile_loc)
	pass

@then('validate presence of fee plan')
def step_presence_of_fee_plan(context):
	pass

@then('validate presence of loan plan')
def step_presence_of_loan_plan(context):
	pass