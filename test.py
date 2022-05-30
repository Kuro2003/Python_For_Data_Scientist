import pandas as pd
import numpy as np

arr = np.random.rand(4,4)
print(arr)
res = np.where(arr>0,arr**2,-2)
print(res)
