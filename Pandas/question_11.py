import pandas as pd

# This code creates a Pandas DataFrame from a dictionary and selects a single column

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)  # pd.DataFrame creates a DataFrame from a dictionary

selected_column = df['Name']  # selected_column selects the 'Name' column from the DataFrame

print(selected_column)
