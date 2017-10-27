Feature: taken one loan, one missed payment and total early repayment

@all
Scenario: To validate presence of fee plan
   Given  a file
   Then   validate presence of fee plan

@all
Scenario: To validate presence of loan plan
   Then   validate presence of loan plan

@all
Scenario: To validate fee plan
   Then   validate fee plan

@all
Scenario: To validate loan plan
   Then   validate loan plan