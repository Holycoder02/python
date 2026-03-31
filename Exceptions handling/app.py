#to use the try-except block to handle exceptions in Python. The try block contains the code that may raise an exception, while the except block contains the code that will be executed if an exception occurs. You can specify the type of exception you want to catch, or you can catch all exceptions using a generic except block.

try:
    # Code that may raise an exception
   num = int(input('Enter a number: '))
   result = 10/ num
   print(f'result: {result}')

except ZeroDivisionError:
   print('Error: Cannot divide by zero.')

except ValueError:
   print('Error: Invalid input. you cannot divide string.')





