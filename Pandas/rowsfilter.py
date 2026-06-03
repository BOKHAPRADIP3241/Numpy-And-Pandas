import pandas as pd

data = {
    "Name" : ["Pradip", "Suman", "Rohit", "Satyam", "Ankit","Rohit", "Satyam", "Ankit"],
    "Age" : [25, 26, 27, 28, 29, 27, 28, 29],
    "City" : ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Bangalore", "Chennai", "Kolkata"],
    "Salary" : [50000, 60000, 70000, 80000, 90000, 70000, 80000, 90000],
    "Performance" : ["Good", "Excellent", "Average", "Good", "Excellent", "Average", "Good", "Excellent"]
}

df = pd.DataFrame(data)

# high_salary = df[df["Salary"] > 75000]
# print("--------------- Employees with salary greater than 45000 ---------------")
# # print(high_salary)


# filtered_multiple_using_and = df[(df["Salary"] > 50000) & (df["Age"] > 20) & (df["Performance"] == "Excellent")]
# print("--------------- Employees with salary greater than 50000, age greater than 20 and performance is excellent ---------------")
# print(filtered_multiple_using_and)



filtered_multiple_using_or = df[(df["Salary"] > 900000) | (df["Age"] > 34)]
print("--------------- Employees with salary greater than 50000, age greater than 20 and performance is excellent ---------------")
print(filtered_multiple_using_or)
