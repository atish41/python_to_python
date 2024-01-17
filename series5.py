#creating series and accessing vslues

import pandas as pd

prices=[1000,2000,3000,4000]
products=["nokia","samsaung","oppo","iphone"]

s=pd.Series(prices,name="mobiles",index=products)
print(s)