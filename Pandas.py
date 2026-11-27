from turtle import fill

import pandas as pd
df = pd.read_csv("messy_orders.csv")
print(df)
print(df.isnull().sum())  
df["CustomerID"].fillna(df["CustomerID"].mean(), inplace=True)  # Fill missing values with the mean
print(df)
df["OrderID"] = df["OrderID"].fillna(0, inplace=True)  # Fill missing values with 0
print(df)
df["Age"] = df["Age"].fillna(df["Age"].median(), inplace=True)  # Fill missing values with the median
print(df)
df["City"] = df["City"].fillna("Unknown", inplace=True)  # Fill missing values with "Unknown"
print(df)
df["Price"] = df["Price"].fillna(df["Price"].mode()[0], inplace=True)  # Fill missing values with the mode
print(df)
df["Age"] = df["Age"].ffill()
print(df)   
df["Age"].fillna(df["Age"].mean(), inplace=True)  # Fill remaining missing values with the mean
print(df)   
df=df.dropna()
print(df.duplicated().sum())
df["CustomerID"] = df["CustomerID"].astype(str)
print(df.dtypes)
df["OrderID"] = df["OrderID"].astype(str)
print(df.dtypes)
df["Age"] = df["Age"].astype(str)
print(df.dtypes)
df["City"] = df["City"].astype(str)
print(df.dtypes)
df["Price"] = df["Price"].astype(str)
print(df.dtypes)
print(df["Age"])
df["Age"] = df["Age"].str.strip()
print(df["Age"])
print(df["Price"])
df["Price"] = df["Price"].str.lower()
print(df["Price"])
print(df["City"])
df["City"] = df["City"].str.title()
print(df["City"])
print(df["CustomerID"])
df["CustomerID"] = df["CustomerID"].str.replace(" ID", "id")
print(df["CustomerID"])
df.sort_values("Age", ascending=True, inplace=True)
print(df["Age"])
df.sort_values("Price", ascending=False, inplace=True)
print(df["Price"])
df.sort_values(["Age","Price"], ascending=[False, False], inplace=True)
print(df["Age"])
print(df["Price"])

num = [1,2,3,4,5,6,7,8,9,10]
def mul(num):
    mul = num*2
    sum = num + 100
    minus = num - 50
    divide = num/2
    return mul, sum, minus, divide
result=list(map(mul,num))
for i in result:
    print(i)
print(df.groupby("City").size())















