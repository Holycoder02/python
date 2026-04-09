"""
Describe method in pandas is used to generate descriptive statistics that summarize the central tendency, dispersion 
and shape of a dataset's distribution, exculding NaN values. 
it provides a quick overview of the data, including measures such as count, mean, standard deviation, minimum, 25th percentile, median 
(50th percentile), 75th percentile, and maximum values for each numerical column in the DataFrame.
the describe() method can be used on both numerical and categorical data, but the output will differ based on the type of data.

step 1: sample data frame

"""
import pandas as pd

data = {
    "Name": ['Ram', 'Shyam', 'Hari', 'gita', 'sita', 'laxmi', 'Raj', 'Ravi'],
    "Age": [ 28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance": [85, 90, 78, 93, 88, 95, 80, 89]


}

df = pd.DataFrame(data)

print("sample DataFrame")
print(df)
print('Descriptive statistics')
print(df.describe())


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