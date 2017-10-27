from behave      import given, when, then
from hamcrest    import assert_that, equal_to


@given('a file')
def step_given_the_file(context):
	AccountID = context.config.userdata.get("accountid")
	CustomerID = context.config.userdata.get("customerid")
	Loan_Amount = context.config.userdata.get("loanamount")
	Term = context.config.userdata.get("term")
	Interest_Rate = context.config.userdata.get("iterest_rate")
	Origination_Fee = context.config.userdata.get("origination_fee")
	pass

@then('validate presence of fee plan')
def step_presence_of_fee_plan(context):
	pass

@then('validate presence of loan plan')
def step_presence_of_loan_plan(context):
	pass

@then('validate fee plan')
def step_fee_plan(context):
	pass

@then('validate loan plan')
def step_loan_plan(context):
	pass