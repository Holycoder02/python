import pandas as pd

#read data from csv file into data frame

#df = pd.read_csv("your_file.csv", encoding="utf-8")

#or
# if your csv file contains special characters, you can use "latin-1" encoding
 
# df = pd.read_csv("your_file.csv", encoding="latin-1")
# print(df)

#for excel file
# df = pd.read_excel("your_file.xlsx")
# print(df)

# to read cloud data we can use the library 
# gcsfs