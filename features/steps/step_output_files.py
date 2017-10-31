from behave      import given, when, then
from hamcrest    import assert_that, equal_to
from transformation import scenario
from files import retrieve_files
from dir_file import dir_create


@given('a file')
def step_given_the_file(context):
	
	accountid = context.config.userdata.get("accountid")
	customerid = context.config.userdata.get("customerid")
	loanid = context.config.userdata.get("loanid")
	masterfile_loc = context.config.userdata.get("masterfile_loc")
	date = context.config.userdata.get("date")
	resultsfiles_loc = context.config.userdata.get("resultsfilelocation")


	
	context.transformation = scenario()
	context.files = retrieve_files()
	interestRate, termlength, fieldsep= context.files.files(date, masterfile_loc)
	dir_file = dir_create()
	values = dir_file.dir(resultsfiles_loc)
	context.transformation.scenario_writing_to_files(accountid, customerid, loanid,fieldsep)
	pass

@then('validate presence of fee plan')
def step_presence_of_fee_plan(context):
	pass

@then('validate presence of loan plan')
def step_presence_of_loan_plan(context):
	pass