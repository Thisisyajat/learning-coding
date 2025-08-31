# The program prints the square and cube of the entered numeric value.
# (C) Yajat Gupta

print('''
Welcome!
This program prints the square and cube of the entered number.
''')
a = float(input("Enter a number ==> "))
print()
print(f"The square of {a} is {a**2}")
print(f"The cube of {a} is {a**3}")
print()
print("Program ran successfully. Exiting.")

# Output
'''
Welcome!
This program prints the square and cube of the entered number.

Enter a number ==> 5

The square of 5.0 is 25.0
The cube of 5.0 is 125.0

Program ran successfully. Exiting.
'''