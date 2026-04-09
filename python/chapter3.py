#operaters

result = 10 + 5 * 2
print(result)

# pythhon operats on based of BDMS

# Arthmetic operators
# +, -, *, /, //, %, **


x =10
y = 20


print(x+y)
print(x-y)
print(x*y)
print(x/y)   #divisin
print(x//y)    #floor division  removes the decimal part and gives the integer part of the result 
print(x%y)    #modulus - remaierder
print(x**y)  #exponentaion for power culculation


#operators

x = 10
y = 5

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#logical operators

# multiple conditions combine - Boolean True/False
# 1 and - all conditions must be true > true
# 2 or - at least one condition> true
# 3  not - single operand - reverses the logical state of its operands

age = 20
is_student =True
print(age>18 and is_student)
print(age> 25 or is_student)
print(not is_student)

#Assigment operators to assgin values to variables
#""""=, +=, -=, *=, /=, //=, %=, **=""""
x =10
print(x)
x += 5
print(x)


#identie operators
#"""" is - True is not - False """"
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b) #true because a and b refer to the same object in memory
print(a is c) #false because a and c refer to different objects in memory
print(a == c) #true because a and c have the same content
print(a is not c) #true because a and c refer to different objects in memory
print(a is not b) #false because a and b refer to the same object in memory
print(a is not a) #falsse because a and a refer to the same object in memory


#membership operators  // only of sequence data types like list, truple, string, set, frozenset, dictionary
#in - true if a seqence contion a specific value
#not in - true if a sequence does not contain a specific value
my_list = [1, 2, 3, 4, 5]
print(3 in my_list) #true because 3 is in the list
print(6 in my_list) #false because 6 is not in the list
print(3 not in my_list) #false because 3 is in the list
print(6 not in my_list) #truse because 6 is not in the list

vegetables = ['carrot', 'broccoli', 'spinach']
print('allo' in vegetables) #false
print('carrot' 'spinach' in vegetables) 

#true because both 'carrot' and 'spinach' are in the list
