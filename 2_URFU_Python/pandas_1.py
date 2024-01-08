import pandas as pd
import numpy as np

arr = np.random.standard_normal((6,4))
df = pd.DataFrame(arr, columns=["A", "B", "C", "D"],
                  index=[1,2,3,4,5,6])
print(df.loc[2:5,["B", "D"]])