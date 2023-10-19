#creating Series using ndarray

import pandas as pd
import numpy as np

values=['a','b','c','d']
data=np.array(values)

print(data)

s=pd.Series(data)

print(s)