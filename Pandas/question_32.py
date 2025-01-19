import pandas as pd

data1 = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']}
data2 = {'ID': [1, 2, 4], 'Age': [25, 30, 40]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

inner_join_df = pd.merge(df1, df2, on='ID', how='inner')

print(inner_join_df)
