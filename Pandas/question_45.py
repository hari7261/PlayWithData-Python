import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

result = df.applymap(lambda x: x * 2)

print(result)
