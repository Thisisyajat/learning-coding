# This program prints the largest number of the three numbers entered by the user.
# Author: Yajat Gupta

def print_largest_number(a, b, c):
    largest = max(a, b, c)
    print("The largest number is:", largest)
    print()
    print("Program ran successfully. Exiting...")

print('''
Welcome to the program!
This program prints the largest number of three numbers entered by the user.
''')
num1 = float(input('Enter the first number ==> '))
num2 = float(input('Enter the second number ==> '))
num3 = float(input('Enter the third number ==> '))
print_largest_number(num1, num2, num3)