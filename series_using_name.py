#creating series object using list,assigning a name

import pandas as pd

m=[56,45,35,41,44,60]

s=pd.Series(m,name="Marks")

print(s)
print(type(s))