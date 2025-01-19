import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

sorted_df = df.sort_values(by='Age')

print(sorted_df)
