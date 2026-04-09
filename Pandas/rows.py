#head() tail()

#head() 5
# tail(n) 5
# if you don't pass any values then, bydefault it will show the first and last (5) rows of the dataframe
# only integer values are allowed in head() and tail() functions


import pandas as pd 
df = pd.read_json("output.json")

print('Display 10 rows of first')
print(df.head(10))

print('Display 10 rows of last')
print(df.tail(10))

"""
how to filtered rows based on condition and how to select specific columns from the filtered rows


"""
data = {
    "Name": ['Ram', 'Shyam', 'Hari', 'gita', 'sita', 'laxmi', 'Raj', 'Ravi'],
    "Age": [ 28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 93, 88, 95, 80, 89]

}
df = pd.DataFrame(data)

high_salary = df[df['Salary'] > 50000]
print('Employees with salry > 50000')
print(high_salary)

#for multiple conditions
filtered = df[(df['Age'] > 30) & (df['Salary'] > 50000)]
print('Employees with age > 30 + salary > 50000')
print(filtered)


#using OR condition

filtered_or = df[(df['Age'] >35) | (df["Performance Score"] > 90)]
print('Employees older than 35 OR oerformance score > 90')
print(filtered_or)
