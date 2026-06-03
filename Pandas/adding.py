import pandas as pd

data = {
    "Name" : ["Pradip", "Suman", "Rohit", "Satyam", "Ankit","Rohit", "Satyam", "Ankit"],
    "Age" : [25, 26, 27, 28, 29, 27, 28, 29],
    "City" : ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Bangalore", "Chennai", "Kolkata"],
    "Salary" : [50000, 60000, 70000, 80000, 90000, 70000, 80000, 90000],
    "Performance" : ["Good", "Excellent", "Average", "Good", "Excellent", "Average", "Good", "Excellent"]
}

df = pd.DataFrame(data)

df["Bonus"] = df["Salary"] * 0.1
print("--------------- DataFrame with Bonus column added ---------------")
print(df)

df.insert(5,"Tax", df["Salary"]*.5)
print("--------------- DataFrame with Tax column added at index 5 ---------------")
print(df)