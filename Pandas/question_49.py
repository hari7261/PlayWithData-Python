import pandas as pd

data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
        'Value': [10, 20, 15, 30, 25]}
df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
resampled_df = df.resample('D').mean()

print(resampled_df)
