try:
    num1 = int(input('enter a number 1 '))
    num2 = int(input('enter a number 2 '))
    try:
        result = num1 / num2
        print(f'Result: {result}')
    except ZeroDivisionError:
        print('you cannot divide by zero')
    
except ValueError:
    print('Invalid input')