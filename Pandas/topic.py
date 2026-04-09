"""
next topic

before we move first we needd to understand 2 things about data frame or data manipulation
1- how big is you data set
2- what are the name of the columns in you data set

 to over come all this pandas provide us with 2 functions we can say that
 
   Shape and columns

   shape is a attribute that returns a tuple representing the dimensionality of the DataFrame.
    columns is a attribute that returns the column labels of the DataFrame as an Index object.
"""

import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Hari', 'gita', 'sita', 'laxmi', 'Raj', 'Ravi'],
    "Age": [ 28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 93, 88, 95, 80, 89]

}

df = pd.DataFrame(data)
print(df)
print(f'Shape: {df.shape}')
print(f'Columns: {df.columns}')
