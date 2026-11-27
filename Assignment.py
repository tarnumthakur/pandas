import pandas as pd
data = {'Name': ['Amit', 'Rahul', 'Priya', 'Neha', 'Amit',
             'Rohit', 'Simran', 'Karan', 'Priya', 'Anjali'],
    'Age': [22, 25, 21, 24, 22, 28, 23, 26, 21, 27],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Pune', 'Delhi',
             'Chandigarh', 'Pune', 'Mumbai', 'Delhi', 'Pune'],
    'Salary': [25000, 35000, 28000, 40000, 25000,
               50000, 32000, 45000, 28000, 38000],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'IT',
                   'IT', 'HR', 'Sales', 'IT', 'HR'],
    'Experience': [1, 3, 1, 4, 1, 6, 2, 5, 1, 4]}

df = pd.DataFrame(data)
df.head(5)
print(df.head(5))
df.tail(3)
print(df.tail(3))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isna().sum())
print(df[['Name','Salary']])
print(df[['Salary']])
print("Max Age: ", df['Age'].max())
print("Min Age: ", df['Age'].min())
print(df[df['Salary'] > 30000])
print(df[(df['Age'].between(22,26))])
print(df[(df["Department"] =="IT" )])
print(df[(df["City"] == 'Delhi' ) & (df['Salary'] > 25000)])
print(df.sort_values(by='Salary', ascending=False))
print(df[df.duplicated()])
df = df.drop_duplicates().reset_index(drop=True)
df['Annual_Salary'] = df['Salary'] * 12
print(df)
df["salary"]=df ['Salary'] * 1.10
print(df)
df= df.rename(columns={'salary':'Monthly_Salary'})
print(df)
print(df.groupby('Department')['Monthly_Salary'].mean())
print(df.loc[df.groupby('Department')['Monthly_Salary'].idxmax()])
print(df.groupby('City')['Monthly_Salary'].sum())
print(df['Department'].value_counts())
print(df[df['Experience'] > 3])
print(df.groupby(['City'])['Department'].size())
print(df.nlargest(3, 'Monthly_Salary'))
def get_level(experience):
    if experience < 2:
        return 'Junior'
    elif experience < 5:
        return 'Mid-level'
    else:
        return 'Senior'
df['Experience_Level'] = df['Experience'].apply(get_level) 
print(df)
print(df.groupby('Department')['Monthly_Salary'].mean().idxmax())
total_salary = df['Monthly_Salary'].sum()
print(df.groupby('Department')['Monthly_Salary'].sum() / total_salary * 100)
summary = df.groupby('Department').agg(
    Employees=('Name', 'count'), 
    Avg_Salary=('Monthly_Salary', 'mean'),
    Total_Salary=('Monthly_Salary', 'sum'),
    Max_Salary=('Monthly_Salary', 'max'),
    Min_Salary=('Monthly_Salary', 'min'))
print(summary)
