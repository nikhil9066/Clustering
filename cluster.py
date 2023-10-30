import pandas as pd
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'washingtonpolice.csv'

df = pd.read_csv(file_path)
print(df)

data_types = df.dtypes
print(data_types)

print(type(df))
print("-----------")
print(df.shape)

description = df.describe() 
print(description)

print(df.info())

print(df.isnull())
print(df.isnull().sum())
print("-----------")
dropdf = df.dropna()
print(dropdf.shape)

print(8770-6810)
print(dropdf.isnull().sum())
print(dropdf.head(4).to_string())

print(dropdf.isna().sum())
print("-----------")

print(dropdf.armed.value_counts())

plt.figure(figsize=(12, 8))
plt.title('Age Distribution of Deaths', fontsize=15)
sns.distplot(dropdf.age)
plt.tight_layout()
plt.show()