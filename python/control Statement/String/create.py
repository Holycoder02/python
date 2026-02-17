name = 'sagar'

name_2 = "Python"

name_3 = '''python is a programing language'''

name_4 = """
this is a
multi line string
"""
print(name, name_2, name_3, name_4)

str = "python is a programming language"
print(len(str))     #len(str) is used to find the length of the string even the space
print(str[0])      #str[0] is used to access the first character of the string
print(str[1])      #str[1] is used to access the second character of
print(str[-1]) #str[-1] is used to access the last character of the string

# slicing
#slicing 
#python

# string }
#start = 0
#stop = 4
#step = 1 2 3 

text = "thisispythonkingofai"
print(text[1:5:1])

#concatenate   only with string
#concatenation
name = "sagar"
ser_name = "lodi"
print('hi', name + ser_name)

str = input('enter your name: ').capitalize()
print('hi', str)

str = input('enter a sentence: ').title()
print(str)

#search in string
#find(sub)

text = "python programming"
print(text.find('i'))  #find() is used to find the index of the first occurrence of the specified substring in the string. If the substring is not found, it returns -1.'))

#replace 

text = "python programming"
print(text.replace('python', 'java'))  #replace() is used to replace all occurrences of a specified substring with another substring in the string. It returns a new string with the replacements made.

text = "you, are, learning, python"
print(text.split(','))  #split() is used to split a string into a list of substrings based on a specified delimiter. It returns a list of substrings. If no delimiter is specified, it splits the string by whitespace.

#join(iterable)

result = ", ".join(['python', 'programming', 'is', 'fun'])  #join() is used to join the elements of an iterable (such as a list) into a single string, with a specified separator between the elements. It returns a new string that is the concatenation of the elements in the iterable, separated by the specified separator.
print(result)


