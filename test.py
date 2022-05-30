import pandas as pd
import numpy as np

data = pd.DataFrame({'Qu1' : [1,3,4,3,4],
                    'Qu1' : [2,3,1,2,3],
                    'Qu2' : [1,5,2,4,4]})
res = data.value_counts()
print(res)