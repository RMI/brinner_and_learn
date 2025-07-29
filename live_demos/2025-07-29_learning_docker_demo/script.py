import numpy as np
import pandas as pd

data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
df = pd.DataFrame(data)

print("Mean of column a:", np.mean(df['a']))
