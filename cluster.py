import pandas as pd

file_path = 'washingtonpolice.csv'

df = pd.read_csv(file_path)
print(df)

description = df.describe()
print(description)

data_types = df.dtypes
print(data_types)