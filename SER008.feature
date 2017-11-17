Feature: Validating the Test Case SER008

  Background: Validate SER008
  Given AccountId "385030" and CustomerId "200812202114" and date "20160510"

   @all
  Scenario: To check the Fee Plan
    When single loan is booked
    then check fee plan in "PortfolioFile"

  @all
  Scenario: To check the Loan Plan
    When single loan is booked
    then check loan plan in "PortfolioFile"

  @all
  Scenario: To validate the Fee Plan
   When single loan is booked
   then validate InterestRate of "14" in "PortfolioFile"
   and validate TermLengthMonths of "12" in "PortfolioFile"

  @all
  Scenario: To validate the Loan Plan
    When single loan is booked
    then validate OriginalPurchaseAmount of "10000" in "PortfolioFile"
    and validate NextPaymentAmount of "847.35" in "PortfolioFile"
    and validate RemainingPayments of "11" in "PortfolioFile"

  @all
  Scenario: To validate multiple Loan Plans
    When multiple loans are booked
    then validate multiple loans in "PortfolioFile"

  @all
  Scenario: To validate Principal Applied for one loan
    When single loan is booked
    then validate Principal applied of "10000" in "PortfolioTransactionFile"

  @all
  Scenario: To validate Principal Applied for multiple loan
    When multiple loans are booked
    then validate Principal applied of "10000" in "PortfolioTransactionFile"

  @all
  Scenario: To validate Monthly fee Applied for one loan
    When single loan is booked
    then validate monthly fee applied of "14" in "PortfolioTransactionFile"

  @all
  Scenario: To validate Monthly fee Applied for multiple loan
    When multiple loans are booked
    then validate monthly fee applied of "14" in "PortfolioTransactionFile"

  @all
  Scenario: To validate Origination fee Applied for one loan
    When single loan is booked
    then validate origination fee applied of "100" in "PortfolioTransactionFile"

  @all
  Scenario: To validate Origination fee Applied for multiple loan
    When multiple loans are booked
    then validate origination fee applied of "100" in "PortfolioTransactionFile"


  @all
  Scenario: To validate Cycle Date for one loan
    When single loan is booked
    then validate for the amount applied to Cycle Date "10" in "AccountFile"

  @all
  Scenario: To validate Cycle Date for multiple loan
    When multiple loans are booked
    then validate for the amount applied to Cycle Date "10" in "AccountFile"

  @all
   Scenario: To check missed payments for single loan
    When single loan is booked
    then validate OutstandingFees applied of "14" in "PortfolioFile"


  @all
  Scenario: To check missed payments for multiple loan
    When multiple loans are booked
    then validate OutstandingFees applied of "14" in "PortfolioFile"

  @all
  Scenario: To check early repayments for single loan
    When single loan is booked
    then validate CurrentDue of "847.35" in "PortfolioFile"


  @all
  Scenario: To check early repayments for multiple loan
    When multiple loans are booked
    then validate CurrentDue of "847.35" in "PortfolioFile"

  @all
  Scenario: To check partial pastdue repayments for single loan
    When single loan is booked
    then validate PastDue of " " in "PortfolioFile"

  @all
  Scenario: To check partial pastdue repayments for multiple loan
    When multiple loans are booked
    then validate PastDue of " " in "PortfolioFile"

  @all
  Scenario: To check total pastdue repayment
    When multiple loans are booked
    then validate PastDue of " " in "PortfolioFile"
