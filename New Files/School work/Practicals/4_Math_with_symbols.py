# The program performs arithmetic operations on two numbers, based on the operator entered by the user.
# (C) Yajat Gupta

print('''
Welcome to the basic calculator program.
This program can perform addition (+), subtraction (-), multiplication (*) and division (/) on two numbers entered by the user.

''')

num1 = float(input('Enter 1st number --> '))
mode = input('Enter the operator from the following options : | + | - | * | / |    --> ')
num2 = float(input('Enter 2nd number --> '))
print()
if mode == '+':
    print(f'{num1} + {num2} = {num1 + num2}')
    print()
    print('Program ran successfully. Exiting...')
elif mode == '-':
    print(f'{num1} - {num2} = {num1 - num2}')
    print()
    print('Program ran successfully. Exiting...')
elif mode == '*':
    print(f'{num1} * {num2} = {num1 * num2}')
    print()
    print('Program ran successfully. Exiting...')
elif mode == '/':
    print(f'{num1} / {num2} = {num1 / num2}')
    print()
    print('Program ran successfully. Exiting...')
else:
    print('Invalid operator. Please rerun the program to continue...')