import pandas as pd

data = {
    'Category': ['A', 'A', 'B', 'B'],
    'Values': [10, 15, 10, 20]
}

df = pd.DataFrame(data)

pivot_table = df.pivot_table(values='Values', index='Category', aggfunc='mean')

print(pivot_table)
