Feature: Loan plan Validation

@all
Scenario: To validate Interest Rate
   Given  a file for validating loan plan
	Then validate interest rate for loan plan

Scenario: To validate TermLengthMonths
	Then validate TermLengthMonths for loan plan

Scenario: To validate OriginalPurchaseAmount
	Then validate OriginalPurchaseAmount

Scenario: To validate NextPaymentAmount
	Then validate NextPaymentAmount

Scenario: To validate RemainingPayments
	Then validate RemainingPayments
