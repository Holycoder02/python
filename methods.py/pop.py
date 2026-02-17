a = [1, 2, 3, 4, 5]
a.pop(0)  #//The pop() method is used to remove and return the last element from a list. It modifies the original list by removing the last item and returns that item. If the list is empty, it raises an IndexError.
print(a)  # Output: [1, 2, 3, 4]

#//to remove through pop method we use the indexing number of the values


a = [1, 2, 3,]
popped = a.pop(0)
print(popped)  # Output: 1
print(a)  # Output: [2, 3]