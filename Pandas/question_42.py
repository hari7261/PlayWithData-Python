import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

def add_columns(row):
    return row['A'] + row['B']

df['C'] = df.apply(add_columns, axis=1)

print(df)
