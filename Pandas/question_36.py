import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice'], 'Age': [25, 30, 35, 25]}
df = pd.DataFrame(data)

df = df.drop_duplicates()

print(df)
