import pandas as pd

price=[5000,2000,10000,12000]
accomdation=["paying gust","cot basis",'flat',"bunglow"]


s=pd.Series(price,name="rental cost in city",index=accomdation)
print(s)