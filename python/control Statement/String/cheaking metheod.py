str = "python"

print(str.startswith('p'))  #startsWith() is used to check if the string starts with the specified prefix. It returns True if the string starts with the prefix, and False otherwise.
print(str.endswith('n'))  #endsWith() is used to check if the string ends with the specified suffix. It returns True if the string ends with the suffix, and False otherwise.
print(str.islower())  #islower() is used to check if all characters in the string are lowercase. It returns True if all characters are lowercase, and False otherwise.
print(str.isupper())  #isupper() is used to check if all characters in the
#string are uppercase. It returns True if all characters are uppercase, and False otherwise.

print(str.isalpha())  #isalpha() is used to check if all characters in the string are alphabetic. It returns True if all characters are alphabetic, and False otherwise.
print(str.isdigit())  #isdigit() is used to check if all characters in the string are digits. It returns True if all characters are digits, and False otherwise.
print(str.isalnum())  #isalnum() is used to check if all characters in
#the string are alphanumeric (either letters or digits). It returns True if all characters are alphanumeric, and False otherwise.

#list
name = "ramesh"
age = 25
marks = 85.5
print(name, age, marks)



#1 square brakets
my_list = [1, 2, 3, 4, 5, "hello", "paython", 3.14, True]
print(my_list)

#2 list() constructor
my_list = list((1, 2, 3, 4, 5, "hello", "paython", 3.14, True))
print(my_list)


#list comperehension and range constructing a list from an iterable
squares = [x**2 for x in range(1, 11)]
print(squares)

#concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2  #//lis_1 + lis_2 will concatenate the two lists and create a new list that contains all the elements from both lists. The original lists remain unchanged.
print(result)

#MEMERSHIP
my_list = [1, 2, 3, 4, 5]
check = int(input('enter a number = '))
if check in my_list:  #//The in operator is used to check if a specified element exists in a list. It returns True if the element is found in the list, and False otherwise.
    print('found')
else:
    print('not found')
#for not in my list............
    lis_2 = [6, 7, 8, 9, 10]
    check = int(input('enter a number - '))
    if check not in lis_2:
        print('yes not found')
    else:        print('found')
        
          
