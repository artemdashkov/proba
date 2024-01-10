import pandas as pd
import numpy as np

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

df = pd.DataFrame(list_1, list_2, columns=["A", "B"],
                  index=[1,2,3])
print(df)