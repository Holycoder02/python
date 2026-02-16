#sequences type data type 
#tupple, list, string,
# 
 



#sting means cotation "" or ''
#its a immutaion , means we cannot change the value of a string once it is created 
#you can  update it tho....


text = 'this is a string'
print(text)
print(type(text))


#in list we can chanr the value of a list and it is mutable data type


my_list =['data1', 'data2', 'data3']
print(my_list)


#tpule is a immutable data type 
my_tuple =('data1', 'data2', 'data3')
print(my_tuple)



#set is a unorderd collection of unique element
# SET(mutable data type)
# frozen set (immutable data type)
#  

unique_numbers ={1, 2, 3, 4, 4, 5,}
print(unique_numbers)



#forzen set
immutable_set = frozenset([1, 2, 3, 3, 4])
print(immutable_set)


#mapping data type its about dictionary data type 
#pair , key1:value2  curly braces 

person = {
    'name': 'raghav', 'age': 30, 'city': 'delhi'
}
print(person)
