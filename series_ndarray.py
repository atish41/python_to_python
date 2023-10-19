#creating ndarray and passign argument

import pandas as pd
import numpy as np

values=[10,20,30,40]
data=np.array(values)

print(data)

s=pd.Series(data)
print(s)