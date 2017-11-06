Feature: Validating the Test Case SER007

  @all
  Scenario: To check the Fee Plan
    Given a file "PortfolioFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
   then check fee plan in "PortfolioFile"

  @all
  Scenario: To check the Loan Plan
    Given a file "PortfolioFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then check loan plan in "PortfolioFile"

  @all
  Scenario: To validate the Fee Plan
   Given a file "PortfolioFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
   When single loan is booked
   then check InterestRate in "PortfolioFile"
   and check TermLengthMonths in "PortfolioFile"

  @all
  Scenario: To validate the Loan Plan
    Given a file "PortfolioFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then check InterestRate in "PortfolioFile"
    and check TermLengthMonths in "PortfolioFile"
    and check OriginalPurchaseAmount in "PortfolioFile"
    and validate NextPaymentAmount of "847.35"
    and validate RemainingPayments of "11"

  @all
  Scenario: To validate multiple Loan Plans
    Given two files "PortfolioFile" "AccountFile" and AccountId "385030" and CustomerId "200812202114"
    When multiple loans are booked
    then check InterestRate in "PortfolioFile"
    and check TermLengthMonths in "PortfolioFile"
    and check OriginalPurchaseAmount in "PortfolioFile"
    and validate NextPaymentAmount of "847.35"
    and validate RemainingPayments of "11"


  @all
  Scenario: To validate Principal Applied for one loan
    Given three files "PortfolioProjectionFile" "AccountFile" "PortfolioTransactionFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then check Principal applied in "PortfolioTransactionFile"

  @all
  Scenario: To validate Principal Applied for multiple loan
    Given three files "PortfolioProjectionFile" "AccountFile" "PortfolioTransactionFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When multiple loans are booked
    then check Principal applied in "PortfolioTransactionFile"


 @all
  Scenario: To validate Monthly fee Applied for one loan
    Given three files "PortfolioProjectionFile" "AccountFile" "PortfolioTransactionFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
   When single loan is booked
    then check monthly fee applied in "PortfolioTransactionFile"

  @all
  Scenario: To validate Monthly fee Applied for multiple loan
    Given three files "PortfolioProjectionFile" "AccountFile" "PortfolioTransactionFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When multiple loans are booked
    then check monthly fee applied in "PortfolioTransactionFile"


  @all
  Scenario: To validate Origination fee Applied for one loan
    Given three files "PortfolioProjectionFile" "AccountFile" "PortfolioTransactionFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then check origination fee applied in "PortfolioTransactionFile"


  @all
  Scenario: To validate Origination fee Applied for multiple loan
    Given two files "PortfolioProjectionFile" "AccountFile" "PortfolioTransactionFile" and AccountId "385030" and CustomerId "200812202114"
    When multiple loans are booked
    then check origination fee applied in "PortfolioTransactionFile"


  @all
  Scenario: To validate Cycle Date for one loan
    Given a file "AccountFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then check for the amount applied to Cycle Date " " in "AccountFile"

  @all
  Scenario: To validate Cycle Date for multiple loan
    Given a file "AccountFile" and AccountId "385030" and CustomerId "200812202114"
    When multiple loans are booked
    then check for the amount applied to Cycle Date " " in "AccountFile"


  @all
  Scenario: To check for missed payments
    Given three files "PortfolioProjectionFile" "AccountFile" "PortfolioTransactionFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then validate OutstandingFees applied of "14"
    and validate RemainingPayments of "9"

  @all
  Scenario: To check for missed payments
    Given three files "PortfolioProjectionFile" "AccountFile" "PortfolioTransactionFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When multiple loans are booked
    then validate OutstandingFees applied of "14"
    and validate RemainingPayments of "9"

  @all
  Scenario: To check for early repayments
    Given three files "PortfolioProjectionFile" "AccountFile" "PortfolioTransactionFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then validate CurrentDue of "847.35"
    and validate RemainingPayments of "9"
    and check TermLengthMonths in "PortfolioFile"


  @all
  Scenario: To check for early repayments
    Given three files "PortfolioProjectionFile" "AccountFile" "PortfolioTransactionFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When multiple loans are booked
    then validate CurrentDue of "847.35"
    and validate RemainingPayments of "9"
    and check TermLengthMonths in "PortfolioFile"

  @all
  Scenario: To check if payment is processed
    Given three files "PortfolioProjectionFile" "AccountFile" "PortfolioTransactionFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When single loan is booked
    then validate CurrentDue of "847.35"
    and validate RemainingPayments of "9"

  @all
  Scenario: To check if payment is processed
    Given three files "PortfolioProjectionFile" "AccountFile" "PortfolioTransactionFile" and AccountId "385030" and CustomerId "200812202114" and LoanId "262901"
    When multiple loans are booked
    then validate CurrentDue of "847.35"
    and validate RemainingPayments of "9"







