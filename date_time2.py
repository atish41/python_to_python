#converting datetime with specific format

import pandas as pd

data={
	"produt":['samsung','iphone','motorola'],
	"status":['success','success','failed'],
	"cost":[10000,50000,15000],
	"PurDate":['02-sep-2019','here date is missing','21-sep-2019']

}

df=pd.DataFrame(data)

df['PurDate']=pd.to_datetime(df['PurDate'],errors='coerce')

print(df.head())
print()
print(df.dtypes)

