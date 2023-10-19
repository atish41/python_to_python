#assiging values in series

import pandas as pd

v=[55,66,88,77,99,22,33]

s=pd.Series(v,name="marks")

print(s)
print(s[0])
print(s[2])