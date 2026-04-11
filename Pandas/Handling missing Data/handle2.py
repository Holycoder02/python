import pandas as pd

data = {
    "Name": ['Ram', None, 'Hari', 'gita', 'sita', 'laxmi', 'Raj', 'Ravi'],
    "Age": [ 28, None, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, None, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, None, 78, 93, 88, 95, 80, 89]

}

df = pd.DataFrame(data)
print(df)

#df.fillna(0, inplace=True)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Performance Score'] = df['Performance Score'].fillna(df['Performance Score'].mean())
print(df)
