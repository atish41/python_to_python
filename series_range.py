#creating series object using range and list

import pandas as pd

r=range(100)
a=list(r)
s=pd.Series(a)
print(s)