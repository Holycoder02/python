#list of number like 1 to 100

""""
range(start, stop, step)

start - 1
stop - 100 
step - 1



"""
#a = tuple(range(1, 100, 1))
#print(a)


#listcompersion

"""
[expersion for iteam in itreable if condition]

e - x * 2
iteam -
itrable - range(1,11)
contidion optional   #like-  if , else if else,,,,

"""
"""
squares =[]
for i in range(1,11):
    squares.append(i ** 2)
    print(squares)


squares = [i ** 2 for i in range(1,11)]
print(squares)
"""

#squares of all even number 

squares = [i ** 2 for i in range(1,40) if i%2 == 0]
print(squares)
