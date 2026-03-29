def add_numbers(a, b):
    result = a + b
    return result

answer = add_numbers(3, 5)
print(answer)

def greet(name, city):  #name, city are parameters
    '''displaying a hi message to user'''  #dcostrings
    print(f'welcome {name} from {city}')    
greet(name="raju", city="delhi")  #positional arugemnet ,keyword arugemnet

#default arugemnet
def greet(name, city="delhi"):  #name, city are parameters
    '''displaying a hi message to user'''  #dcostrings
    print(f'welcome {name} from {city}')
greet(name="raju", city="mumbai")  #default arugemnet
greet(name="raju", city="mumbai")  #keyword arugemnet