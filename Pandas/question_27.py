import pandas as pd

data = {'Category': ['A', 'A', 'B', 'B'], 'Subcategory': ['X', 'Y', 'X', 'Y'], 'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data)

grouped_df = df.groupby(['Category', 'Subcategory']).sum()

print(grouped_df)
