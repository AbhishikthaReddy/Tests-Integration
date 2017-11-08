Feature: Fee plan Validation

@all
Scenario: To validate Interest Rate
   Given  a file for validating fee plan
	Then validate interest rate for fee plan

Scenario: To validate TermLengthMonths
	Then validate TermLengthMonths for fee plan
