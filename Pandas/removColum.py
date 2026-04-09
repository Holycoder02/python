import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Hari', 'gita', 'sita', 'laxmi', 'Raj', 'Ravi'],
    "Age": [ 28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 93, 88, 95, 80, 89]

}

df = pd.DataFrame(data)
print(df)

# df.drop(columns=["column_name"], inplace=True)
# df.drop("column_name", axis=1, inplace=True)

# to remove single column
print('Modified Data')
df.drop(columns=["Performance Score", "Age"], inplace=True)
print(df)