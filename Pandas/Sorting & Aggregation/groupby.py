import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karun', 'Narun', 'Marun'],
    "Age": [28, 34, 22,34, 28],
    "salary": [50000, 60000, 45000, 52000, 48000]

}

df = pd.DataFrame(data)
grouped = df.groupby("Age")["salary"].sum()
print(grouped)


"""
df.groupby("Age")
age = 22 > [45000]
age = 28 [50000, 48000] = 98000
age = 34 [60000, 52000] = 112000
"""

"""
for multiple column sorting with aggregation..

import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karun', 'Narun', 'Marun'],
    "Age": [28, 34, 22,34, 28],
    "salary": [50000, 60000, 45000, 52000, 48000]

}

df = pd.DataFrame(data)
grouped = df.groupby(["Age", "Name"])["salary"].sum()
print(grouped)


in this case we are grouping by both age and name and then summing the salary for each group. the
output will show the total salary for each unique combination of age and name.
since each name is unique in this example, the output will show the salary

for each individual name along with thier correspondig age.
"""