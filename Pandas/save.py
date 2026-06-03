import pandas as pd

data = {
    "Name" : ["Pradip", "Suman", "Rohit", "Satyam"],
    "Age" : [25, 26, 27, 28],
    "City" : ["Delhi", "Mumbai", "Bangalore", "Chennai"]
}

df = pd.DataFrame(data)
# df.to_csv("data.csv",index=False)
# print(df)
# print(df.info())

print(df.shape)
print(df.columns)
print(df.dtypes)