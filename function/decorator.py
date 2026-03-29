def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called")
    return wrapper

@my_decorator
def Say_hello():
    print("hello")

Say_hello()

## generator
def count_down(num):
    while num > 0:
        yield num  # yield values one at a time 
        num -= 1

# using the generator
for number in count_down(3):
    print(number)