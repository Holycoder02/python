import pandas as pd
#adding columns to data frame
data = {
    "Name": ['Ram', 'Shyam', 'Hari', 'gita', 'sita', 'laxmi', 'Raj', 'Ravi'],
    "Age": [ 28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 93, 88, 95, 80, 89]

}

df = pd.DataFrame(data)
# Square Brackets[] df["coluumn_name"] = some_Data
print(df)

df["Bonus"] = df["Salary"] * 0.1
print(df)

#using insert() method to add column at specific position
# df.insert(loc=position, column='column_name', value=some_data)

df.insert(0, "Employee ID", [1, 2, 3, 4, 5, 6, 7, 8])
print(df)

"""
updating existing column values
.loc[] 
df.loc[row_index, "column_name"] = new_value

to updated multiple values there are two ways and conditions
1. using loc[] with condition
2. using loc[] with boolean indexing

"""

df.loc[6, "Salary"] = 65000
print(df)

#increasing Salary by 5%
df['Salary'] = df['Salary'] * 1.05

print(df)

