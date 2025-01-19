import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

df['City'] = ['New York', 'Los Angeles', 'Chicago']

print(df)
