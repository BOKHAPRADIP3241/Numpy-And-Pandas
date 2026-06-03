import pandas as pd

data = {
    "Name" : ["Pradip", "Suman", "Rohit", "Satyam", "Ankit","Rohit", "Satyam", "Ankit"],
    "Age" : [25, 26, 27, 28, 29, 27, 28, 29],
    "City" : ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Bangalore", "Chennai", "Kolkata"],
    "Salary" : [50000, 60000, 70000, 80000, 90000, 70000, 80000, 90000],
    "Performance" : ["Good", "Excellent", "Average", "Good", "Excellent", "Average", "Good", "Excellent"]
}

df = pd.DataFrame(data)
print(df)
name = df["Name"]

print("--------------- Single column return series ---------------")
print(name)


subset = df[["Name", "Salary", "Performance"]]
print("--------------- Subset with name and salry, performance ---------------")
print(subset)

