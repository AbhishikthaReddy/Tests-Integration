Feature: ITL001

  Background: Validate ITL001
  Given AccountId "3850330" and CustomerId "200812202114" and date "20160610"
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
  Scenario: To validate multiple Loan Plans
    When multiple loans are booked
    then validate multiple loans in "PortfolioFile"

  @all
  Scenario: To validate Principal Applied for one loan
    then validate Principal applied of "10000" in "PortfolioTransactionFile"

  @all
  Scenario: To validate Principal Applied for multiple loan
    When multiple loans are booked
    then validate Principal applied of "10000" in "PortfolioTransactionFile"

  @all
  Scenario: To validate Monthly fee Applied for one loan
    then validate monthly fee applied of "14" in "PortfolioTransactionFile"

  @all
  Scenario: To validate Monthly fee Applied for multiple loan
    When multiple loans are booked
    then validate monthly fee applied of "14" in "PortfolioTransactionFile"

  @all
  Scenario: To validate Origination fee Applied for one loan
    then validate origination fee applied of "100" in "PortfolioTransactionFile"

  @all
  Scenario: To validate Origination fee Applied for multiple loan
    When multiple loans are booked
    then validate origination fee applied of "100" in "PortfolioTransactionFile"

  @all
  Scenario: To validate Cycle Date for one loan
    then validate for the amount applied to Cycle Date "10" in "AccountFile"

  @all
  Scenario: To validate Cycle Date for multiple loan
    When multiple loans are booked
    then validate for the amount applied to Cycle Date "10" in "AccountFile"