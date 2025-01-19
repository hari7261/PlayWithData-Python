import pandas as pd

data = {'Category': ['A', 'A', 'B', 'B'], 'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data)

result = df.groupby('Category').agg(
    mean_value=('Value', 'mean'),
    sum_value=('Value', 'sum'),
    count_value=('Value', 'count')
)

print(result)
