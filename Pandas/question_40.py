import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

print(df)
