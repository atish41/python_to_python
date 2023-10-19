#creating series object and name and index

import pandas as pd

prices=[1000,2000,3000,4000]
products=["nokia","samsung","oppo,","iphone 6"]

s=pd.Series(prices,name='mobiles',index=products)
print(s)