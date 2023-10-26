#if date time is missing

import pandas as pd

data={
	"product":["samsung","iphone","motorola"],
	"status":["success","success","failed"],
	"cost":[10000,50000,15000],
	"PurDate":['02-sep-2019','here date is missing','21-sep-2019']

}

df=pd.DataFrame(data)

print()
print(df.dtypes)