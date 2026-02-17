#cloneing

list_1 = [1, 2, 3, 4, 5]
list_2 = list_1  #//This creates a new reference to the same list object in memory. Both list_1 and list_2 point to the same list, so changes made through one reference will affect the other.
print(list_2)  # Output: [1, 2, 3, 4, 5]


#copying
list_1 = [1, 2, 3, 4, 5]
list_2 = list_1

list_2 [0] = 100
print(list_1, list_2)  # Output: [100, 2, 3, 4, 5] [100, 2, 3, 4, 5]


#the again for one paticular list to change the value of list_2 but not list_1
list_1 = [1, 2, 3, 4, 5]
list_2 = list_1.copy()  #//The copy() method creates a shallow copy of the list, which means it creates a new list object with the same elements as the original list. Changes made to the new list will not affect the original list.
list_2 [0] = 100
print(list_1, list_2)  # Output: [1, 2, 3, 4, 5] [100, 2, 3, 4, 5]  

#goal achieved



