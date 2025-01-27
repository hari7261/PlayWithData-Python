import pandas as pd

# This code creates a Pandas DataFrame from a dictionary and prints it

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)  # pd.DataFrame creates a DataFrame from a dictionary

print(df)  # print displays the DataFrame
