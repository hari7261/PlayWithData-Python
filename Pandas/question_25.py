import pandas as pd
import numpy as np

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, np.nan, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', np.nan]}
df = pd.DataFrame(data)

df['Age'].fillna(df['Age'].mean(), inplace=True)

print(df)
