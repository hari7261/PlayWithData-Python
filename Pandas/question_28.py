import pandas as pd

data = {'Category': ['A', 'A', 'B', 'B'], 'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data)

grouped_df = df.groupby('Category').agg(['mean', 'sum', 'count'])

print(grouped_df)
