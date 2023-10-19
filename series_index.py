#creating series by column from dataframe

#if we select single column from dataframe then it returns series object

#creating series object and giving name and index
import pandas as pd
v=[145,142,38,13]
i=[10,20,30,40]

s=pd.Series(v,name='counts',index=i)
print(s)