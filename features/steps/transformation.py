import pandas as pd
import os

class scenario(object):

	def __init__(self):
		self.fn = None


	def scenario_writing_to_files(self,accountid,customerid,loanid,originalpurchaseamount,disbursementdate, masterfile_loc):

		#fee plan and loan plan check
		for root, dirs, files in os.walk("data/PortfolioFile"):
			for file in files:
				files1=os.path.basename(file)
				full_path = os.path.join(root, files1)
				read_f=pd.read_csv(full_path,sep="|")
				df=pd.DataFrame(read_f)
				for i in range(len(df['AccountID'])):
					if str(df['AccountID'][i]) == str(accountid) and str(df['CustomerID'][i])== str(customerid) and str(df['LoanID'][i])==str(loanid):
						if str(df['InterestRate'][i])=="0.14" and str(df['DisbursementDate'][i])==disbursementdate and str(df['OriginalPurchaseAmount'][i])==originalpurchaseamount and (df['TermLengthMonths'][i])=="12" :
							if df['PortfolioTransactionId'][i]==0:
								print("This is in fee plan")
							else:
								print("This is in loan plan")
						else:
							print("Mismatch data")
					else:
						print("Mismatch AccountID or CustomerID or LoanID")



