#pandas_test.py

import pandas as pd
import numpy as np
print(pd.__version__)

# Page 3: DataFrame
data = {"name": ["Amit", "Riya"],"salary": [50000, None],"dept": ["IT", "HR"]}
df = pd.DataFrame(data)
print(df)

# Page 4 - reading and writing file
import pandas as pd
df = pd.read_csv("clean_sleep_dataset.csv")

print(df.head())      # first 5
print(df.tail())      # last 5
print(df.shape)       # (rows, cols)
print(df.columns)     # all column names
print(df.dtypes)      # data types
print(df.info())      # null + type summary
print(df.describe())  # stats
print(df.isna().sum()) # how many blank

# Page 5-6
import pandas as pd
df = pd.read_csv("clean_sleep_dataset.csv")

print(df["Sleep Quality"]) # one column - replace with your actual column name
print(df[["Age","Sleep Quality"]]) # two columns

print(df.loc[0]) # first row by label
print(df.iloc[0]) # first row by position
print(df.loc[0:2, ["Age","Sleep Quality"]])

# Filtering - your notes rule: use () & &
print(df[df["Age"] > 30]) # simple
# print(df[(df["Age"]>30) & (df["Sleep Quality"]>7)]) # multi condition

# Page 8: fill missing
df["salary"] = df["salary"].fillna(50000)
(df)