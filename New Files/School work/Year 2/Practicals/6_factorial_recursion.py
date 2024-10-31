# This program prints the factorial of the number entered by the user, using 'recursion' method.
# (C) Yajat Gupta

def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

print('''
This program prints the factorial of the number entered by the user, using 'recursion' method.

''')
n = int(input("Enter the number for which the factorial is to be generated --> "))
print(f'The factorial of {n} is --> {factorial(n)}')
print("Program ran successfully. Exiting...")

# Output
'''

This program prints the factorial of the number entered by the user, using 'recursion' method.


Enter the number for which the factorial is to be generated --> 5
The factorial of 5 is --> 120
Program ran successfully. Exiting...
'''