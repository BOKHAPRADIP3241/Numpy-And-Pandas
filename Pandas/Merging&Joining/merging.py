import pandas as pd

df_customer = pd.DataFrame({
    "CustomerID" : [1, 2, 3, 4],
    "Name" : ["Pradip", "Suman", "Rohit", "Satyam"],
    "City" : ["Delhi", "Mumbai", "Bangalore", "Chennai"]
})

df_orders = pd.DataFrame({
    "OrderID" : [101, 102, 103, 104],
    "CustomerID" : [1, 2, 2, 3],
    "Product" : ["Laptop", "Phone", "Tablet", "Headphones"],
    "Amount" : [1000, 500, 300, 200]
})

df_merged = pd.merge(df_customer, df_orders, on = "CustomerID", how = "inner")
print("--------------- Inner Join ---------------")
print(df_merged)
df_merged = pd.merge(df_customer, df_orders, on = "CustomerID", how = "outer")
print("--------------- Outer Join ---------------")
print(df_merged)
df_merged = pd.merge(df_customer, df_orders, on = "CustomerID", how = "left")
print("--------------- Left Join ---------------")
print(df_merged)
df_merged = pd.merge(df_customer, df_orders, on = "CustomerID", how = "right")
print("--------------- Right Join ---------------")
print(df_merged)    
