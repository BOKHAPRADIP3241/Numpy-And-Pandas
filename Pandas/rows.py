import pandas as pd

df = pd.read_json("sample_Data.json")

print("first 10 rows of the dataframe")
print(df.head())

print("last 10 rows of the dataframe")
print(df.tail())

