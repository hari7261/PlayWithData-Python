import pandas as pd

# This code creates a Pandas DataFrame from a dictionary and selects multiple columns

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)  # pd.DataFrame creates a DataFrame from a dictionary

selected_columns = df[['Name', 'City']]  # selected_columns selects the 'Name' and 'City' columns from the DataFrame

print(selected_columns)
