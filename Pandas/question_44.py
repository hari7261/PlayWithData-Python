import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 95]
}

df = pd.DataFrame(data)

melted_df = pd.melt(df, id_vars=['Name'], value_vars=['Age', 'Score'])

print(melted_df)
