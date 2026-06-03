#importing necessary libraries

import pandas as pd
import numpy as np

#loading the dataset
employee_data = pd.read_csv('Indian Employe Dataset\employees.csv')
print(employee_data)

#checking for missing values
print("Missing values in each column:")
print(employee_data.isnull().sum())

# employee_data['First Name'].fillna(employee_data['First Name'].unique()[0], inplace=True)
# employee_data['Gender'].fillna(employee_data['Gender'].unique()[0], inplace=True)
# employee_data['Senior Management'].fillna(employee_data['Senior Management'].unique()[0], inplace=True)
# employee_data['Team'].fillna(employee_data['Team'].unique()[0], inplace=True)

# employee_data.replace(np.inf,  -np.inf, inplace=True)
# employee_data.fillna(employee_data.mean(), inplace=True)

#removing duplicates
employee_data.drop_duplicates(inplace=True)

#replace low salary values with the mean salary
mean_salary = employee_data['Salary'].mean()
employee_data['Salary'] = employee_data['Salary'].apply(lambda x: mean_salary if x < 10000 else x)

#saving the cleaned dataset
employee_data.to_csv('Indian Employe Dataset\cleaned_employees.csv', index=False)
print("Data cleaning completed. Cleaned dataset saved as 'cleaned_employees.csv'.")



