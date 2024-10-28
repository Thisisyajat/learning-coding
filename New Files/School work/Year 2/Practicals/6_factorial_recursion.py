# This program prints the factorial of the number entered by the user, using 'recursion' method.
# (C) Yajat Gupta
a = 1
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
print()
n = int(input("Enter the number for which the factorial is to be generated --> "))
print(f'The factorial of {n} is --> {factorial(n)}')