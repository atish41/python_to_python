import pandas as pd

df1=pd.read_csv(r"D:\dataset\Data.csv")

a=df1['Country']=="france"
df2=df1.loc[a,'Salary':'Age']

print(df2.head())