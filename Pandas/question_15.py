import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

selected_rows = df.loc[df['Age'] > 25]

print(selected_rows)
