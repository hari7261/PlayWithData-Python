import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

selected_rows = df[df['Age'] > 30]

print(selected_rows)
