from behave      import *
from hamcrest    import assert_that, equal_to

@given('a file "{file}" and AccountID "{AccountID}" and CustomerID "{CustomerID}" and LoanID "{LoanID}"')
def step_one_file(context,file,AccountID,CustomerID,LoanID):
	pass

@given('a file "{file}" and AccountID "{AccountID}" and CustomerID "{CustomerID}"')
def step_one_file(context,file,AccountID,CustomerID):
	pass

@given('two files "{file1}" "{file2}" and AccountID "{AccountID}" and CustomerID "{CustomerID}" and LoanID "{LoanID}"')
def step_two_files(context,file1,file2,AccountID,CustomerID,LoanID):
	pass

@given('two files "{file1}" "{file2}" and AccountID "{AccountID}" and CustomerID "{CustomerID}"')
def step_two_files(context,file1,file2,AccountID,CustomerID):
	pass

@given('three files "{file1}" "{file2}" "{file3}" and AccountID "{AccountID}" and CustomerID "{CustomerID}" and LoanID "{LoanID}"')
def step_three_files(context, file1,file2,file3,AccountID,CustomerID,LoanID):
	pass

@when('single loan is booked')
def step_the_values_are(context):
	pass

@when('multiple loans are booked')
def step_multiple_loans(context):
    pass

@then('check fee plan in "{file1}"')
def step_check_fee_plan_for(context,file1):
	pass

@then('check loan plan in "{file1}"')
def step_check_loan_plan_for(context, file1):
	pass

@then('check InterestRate in "{file1}"')
def step_check_interest_rate_applied_for(context, file1):
	pass

@then('check TermLengthMonths in "{file1}"')
def step_termlengthmonths_for(context, file1):
	pass

@then('check OriginalPurchaseAmount in "{file1}"')
def step_check_originalpurchaseamount_for(context,file1):
	pass

@then('validate NextPaymentAmount of "{NextPaymentAmount}"')
def step_check_nextpaymentamount_for(context,NextPaymentAmount):
	pass

@then('validate RemainingPayments of "{RemainingPayments}"')
def step_check_remainingpayments_for(context,RemainingPayments):
	pass


@then('check Principal applied in "{file1}"')
def step_check_principal_applied(context,file1):
	pass

@then('check monthly fee applied in "{file1}"')
def step_check_monthly_fee(context,file1):
	pass

@then('check origination fee applied in "{file1}"')
def step_check_origination_fee(context,file1):
	pass

@then('check for the amount applied to Cycle Date " " in "{file1}"')
def step_check_cycle_date(context,file1):
	pass

@then('validate OutstandingFees applied of "{Outstandingfees}"')
def step_check_cycle_date(context,Outstandingfees):
	pass

@then('validate CurrentDue of "{CurrentDue}"')
def step_check_cycle_date(context,CurrentDue):
	pass





















