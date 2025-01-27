import pandas as pd

# This code creates a Pandas DataFrame from a dictionary and prints the data types of its columns

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)  # pd.DataFrame creates a DataFrame from a dictionary

print(df.dtypes)  # dtypes returns the data types of each column in the DataFrame
