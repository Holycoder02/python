#continatinoal statement.........
num_1 = float(input('enter number 1 = '))
num_2 =float(input('enter number 2 = '))

choice = input('enter your choice +, -, *, /, //, % = ')

if choice == '+':
    print(f'Addition: {num_1 + num_2}')
    
elif choice == '-':
    print(f'Subtraction: {num_1 - num_2}')

elif choice == '*':
    print(f'Multiplication: {num_1 * num_2}')

elif choice == '/':
    print(f'Division: {num_1 / num_2}')

elif choice == '//':
    print(f'Floor Division: {num_1 // num_2}')

elif choice == '%':
    print(f'Modulus: {num_1 % num_2}')
    

else:
    print('IN-valid choice')
