from behave      import given, when, then
from hamcrest    import assert_that, equal_to
from transformation import scenario


@given('a file')
def step_given_the_file(context):
	context.transformation = scenario()
	accountid = context.config.userdata.get("accountid")
	customerid = context.config.userdata.get("customerid")
	loanid = context.config.userdata.get("loanid")
	interest_rate = context.config.userdata.get("interest_rate")
	termlengthmonths=context.config.userdata.get("termlengthmonths")
	originalpurchaseamount = context.config.userdata.get("originalpurchaseamount")
	disbursementdate = context.config.userdata.get("disbursementdate")
	masterfile_loc=context.config.userdata.get("masterfile_loc")
	resultsfiles_loc = context.config.userdata.get("resultsfiles_loc")
	date=context.config.userdata.get("date")
	context.transformation.scenario_writing_to_files(accountid,customerid,loanid,interest_rate,termlengthmonths,originalpurchaseamount,disbursementdate,resultsfiles_loc)
	pass

@then('validate presence of fee plan')
def step_presence_of_fee_plan(context):
	pass