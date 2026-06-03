import pandas as pd

data = {
    "Name" : ["Pradip", None, "Rohit", "Satyam", "Ankit","Rohit", "Satyam", "Ankit"],
    "Age" : [25, None, 27, 28, 29, 27, 28, 29],
    "City" : ["Delhi", None, "Bangalore", "Chennai", "Kolkata", "Bangalore", "Chennai", "Kolkata"],
    "Salary" : [50000, 60000, 70000, 80000, 90000, 70000, 80000, 90000],
    "Performance" : ["Good", None, "Average", "Good", "Excellent", "Average", "Good", "Excellent"]
}

df = pd.DataFrame(data)
print(df)

df.sort_values(by = ["Age", "Salary"], ascending = [True, False], inplace = True)
print("--------------- DataFrame sorted by Age in descending order ---------------")
print(df)

avg_salary = df["Salary"].mean()
print(avg_salary)