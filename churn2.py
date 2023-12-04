#understand categorical data

import pandas as pd

df=pd.read_csv("D:\Python_Satish_Gupta\D_danial\Machine learning\ml_pipeline\dataset1\data.csv")

df["churn"]=df["churn"].replace(('yes','no',(1,0)))

result1=df.select_dtypes(include=['object'])
print(result1.dtypes)