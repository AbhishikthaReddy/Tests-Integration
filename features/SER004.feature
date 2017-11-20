Feature: SER004

  Background: Validate SER004
  Given AccountId "385030" and CustomerId "200812202114" and date "20160510"
  When single loan is booked

  @all
  Scenario: To check the Fee Plan
    then check fee plan in "PortfolioFile"

  @all
  Scenario: To check the Loan Plan
    then check loan plan in "PortfolioFile"

  @all
  Scenario: To validate the Fee Plan
   then validate InterestRate of "14" in "PortfolioFile"
   and validate TermLengthMonths of "12" in "PortfolioFile"

  @all
  Scenario: To validate the Loan Plan
    then validate OriginalPurchaseAmount of "10000" in "PortfolioFile"
    and validate NextPaymentAmount of "847.35" in "PortfolioFile"
    and validate RemainingPayments of "11" in "PortfolioProjectionFile" for date "20160610"

  @all
  Scenario: To validate Principal Applied for one loan
    then validate Principal applied of "10000" in "PortfolioTransactionFile"

  @all
  Scenario: To validate Monthly fee Applied for one loan
    then validate monthly fee applied of "14" in "PortfolioTransactionFile"

  @all
  Scenario: To validate Origination fee Applied for one loan
    then validate origination fee applied of "100" in "PortfolioTransactionFile"

  @all
  Scenario: To validate Cycle Date for one loan
    then validate for the amount applied to Cycle Date "10" in "AccountFile"

  @all
   Scenario: To check for missed payments
    then validate OutstandingFees applied of "14" in "PortfolioFile"

  @all
  Scenario: To check for early repayments
    then validate CurrentDue of "847.3" in "PortfolioFile"
