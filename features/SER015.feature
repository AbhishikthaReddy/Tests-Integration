Feature: Validating the Test Case SER0015

  @all
  Scenario: To check the Fee Plan
    Given AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then check fee plan in "PortfolioFile"

  @all
  Scenario: To check the Loan Plan
    Given AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then check loan plan in "PortfolioFile"

  @all
  Scenario: To validate the Fee Plan
   Given AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
   When single loan is booked
   then validate InterestRate of "14" in "PortfolioFile"
   and validate TermLengthMonths of "12" in "PortfolioFile"

  @all
  Scenario: To validate the Loan Plan
    Given AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then validate OriginalPurchaseAmount in "PortfolioFile"
    and validate NextPaymentAmount of "847.35" in "PortfolioFile"
    and validate RemainingPayments of "11" in "PortfolioFile"

  @all
  Scenario: To validate Principal Applied for one loan
    Given AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then validate Principal applied in "PortfolioTransactionFile"

  @all
  Scenario: To validate Monthly fee Applied for one loan
    Given AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then validate monthly fee applied in "PortfolioTransactionFile"

  @all
  Scenario: To validate Origination fee Applied for one loan
    Given AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then validate origination fee applied in "PortfolioTransactionFile"

  @all
  Scenario: To validate Cycle Date for one loan
    Given AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then validate for the amount applied to Cycle Date "10" in "AccountFile" and "PortfolioFile"

  @all
   Scenario: To check for missed payments
    Given AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then validate OutstandingFees applied of "14" in "PortfolioFile"

  @all
  Scenario: To check for early repayments
    Given AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then validate CurrentDue of "847.35" in "PortfolioFile"

  @all
  Scenario: To check partial pastdue repayments for multiple loan
    Given AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then validate PastDue of " " in "PortfolioFile"

  @all
  Scenario: To check total pastdue repayment
    Given AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then validate PastDue of " " in "PortfolioFile"
