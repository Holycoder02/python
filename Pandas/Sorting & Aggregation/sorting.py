"""
sorting data 
Sorting data 1 column, or by the method of sorting as sort_values() method
is used to sort the data in 1 colunm or more than 1 column. By default it is in ascending order but we can also sort in descending order by using the parameter ascending=False

syntax: df.sort_values(by="column_name", ascending/descending= true/false, inplace = True) if False then asccending order
if True then descending order))

for multiple column sorting 
syntax: df.sort_values(by=["column_name1", "column_name2", column_name3"], ascending=True/False, inplace = True)


"""

import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Karun'],
    "Age": [28, 34, 22],
    "salary": [10000, 20000, 15000]

}

df = pd.DataFrame(data)
df.sort_values(by="Age", ascending=False, inplace=True)
print('Sorte Age by descending order')
print(df)

#df.sort_values(by="Age", ascending=True/False, inplace=True)




