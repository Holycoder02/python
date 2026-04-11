"""
df["column_name"].count() - it will count the number of non-null values in the column
df["Column_name"].mean() - it will calculate the average of the values in the column
df["column_name"].sum() - it will calculate the total sum of the values in the column
df["column_name"].min() - it will find the minimum value in the column
df["column_name"].max() - it will find the maximum value in the column
df["column_name"].std() - it will calculate the standard deviation of the values in the column
df["column_name"].var() - it will calculate the variance of the values in the column
df["column_name"].median() - it will calculate the median of the values in the column



"""

import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karun'],
    "Age": [28, 34, 22],
    "salary": [10000, 20000, 15000]

}

df = pd.DataFrame(data)

avg_salary = df["salary"].mean()
print(avg_salary)
      