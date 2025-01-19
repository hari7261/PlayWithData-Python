import pandas as pd

data = {'Category': ['A', 'B', 'A', 'B'], 'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data)

grouped_df = df.groupby('Category').mean()

print(grouped_df)
