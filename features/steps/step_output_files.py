from behave      import given, when, then
from hamcrest    import assert_that, equal_to
from transformation import scenario
from files import retrieve_files
from dir_file import dir_create


@given('a file')
def step_given_the_file(context):
	
	masterfile_loc = context.config.userdata.get("masterfile_loc")
	date = context.config.userdata.get("date")
	resultsfiles_loc = context.config.userdata.get("resultsfilelocation")
	input_json_data = context.config.userdata.get("input_data_file")
	
	context.transformation = scenario()
	context.files = retrieve_files()
	dir_file = dir_create()

	termlength, fieldsep = context.files.files(date, masterfile_loc)
	today_now = dir_file.dir(resultsfiles_loc)
	context.transformation.scenario_writing_to_files(termlength, fieldsep, masterfile_loc, today_now, resultsfiles_loc, input_json_data)

	pass

@then('validate presence of fee plan')
def step_presence_of_fee_plan(context):
	pass

@then('validate presence of loan plan')
def step_presence_of_loan_plan(context):
	pass

@then('validate fee plan')
def step_validate_fee_plan(context):
	pass

@then('validate loan plan')
def step_validate_loan_plan(context):
	pass