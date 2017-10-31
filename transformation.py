import pandas as pd
import os

for root, dirs, files in os.walk("C:\\Users\\atlantaadmin\\Desktop\\Orion\\Kabbage1\\Tests-Integration\\data\\PortfolioFile\\"):
    for file in files:
        files1=os.path.basename(file)
        full_path = os.path.join(root, files1)
        read_f=pd.read_csv(full_path,sep="|")
        df=pd.DataFrame(read_f)
        for i in df['PortfolioTransactionId']:
            if i==0:
                print(df.values[i],"fee plan----------------")
            else:
                print("loan plan")


