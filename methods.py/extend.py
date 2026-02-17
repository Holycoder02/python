a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
a.extend(b)  #//The extend() method is used to add all the elements of an iterable (such as a list, tuple, or set) to the end of the list. It modifies the original list by adding each element from the iterable as individual items.
print(a)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]