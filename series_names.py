#creating series object using list, assigning a name

import pandas as pd

m=["Prasad","Daniel","Samual","viay"]
s=pd.Series(m,name="students")
print(s)