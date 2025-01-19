import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Birthdate': ['1990-01-01', '1985-05-15', '1992-07-20']}
df = pd.DataFrame(data)

df['Birthdate'] = pd.to_datetime(df['Birthdate'])
df['Year'] = df['Birthdate'].dt.year
df['Month'] = df['Birthdate'].dt.month
df['Day'] = df['Birthdate'].dt.day

print(df)
