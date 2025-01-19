import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Birthdate': ['1990-01-01', '1985-05-15', '1992-07-20', '1988-03-10']}
df = pd.DataFrame(data)

df['Birthdate'] = pd.to_datetime(df['Birthdate'])
filtered_df = df[(df['Birthdate'] >= '1985-01-01') & (df['Birthdate'] <= '1990-12-31')]

print(filtered_df)
