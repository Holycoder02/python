#programming_language = {
 #   "python": {"name": "Python", "type": "High-level", "paradigm": ["Object-oriented", "Procedural", "Functional"]},
  #  "java": {"name": "Java", "type": "High-level", "paradigm": ["Object-oriented", "Procedural"]},
   # "javascript": {"name": "JavaScript", "type": "High-level", "paradigm": ["Event-driven", "Functional", "Imperative"]},
#}

#print(programming_language)


#chapter - 8 function 
#the maiin advantage of funciton is reseuseability of the code which makes less code to write
#a = 10
#b = 20  
#print(a+b)


#a = 30
#b = 40
#print(a+b)  

#to create a fuction we use a keyword def followed by the function name and parentheses which may include parameters
#def add_numbers(a, b):
 #   return a + b

#or we can also write the above code as
def greete():
    '''displaying a hi message to user'''
    print('hi')
greete()

#modularity
# def add_numbers(a, b):
 #   return a + b    

#scoping
#def outer_function():
 #   x = 10  # This variable is local to outer_function
  #  def inner_function():
   #     y = 20  # This variable is local to inner_function
    #    return x + y  # Accessing x from the outer scope
    #return inner_function()