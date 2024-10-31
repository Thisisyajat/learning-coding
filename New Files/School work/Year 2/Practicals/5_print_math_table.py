# The program generates a table of the number entered by the user.
# (C) Yajat Gupta

# The program generates a table of the number entered by the user.
# (C) Yajat Gupta

print('''
This program generates a table of the integer number entered by the user.
''')

try:
    number = int(input("Enter the number for which the table is to be generated --> "))
    times = int(input("Enter number of times the table should be printed --> "))
    print()
except ValueError:
    print("Invalid input. Please enter a number.")
    exit(0)

for i in range(1, times + 1):
    print(f"{number} × {i} = {number * i}")

print("Program ran successfully. Exiting..")

# Output
'''

This program generates a table of the integer number entered by the user.

Enter the number for which the table is to be generated --> 5
Enter number of times the table should be printed --> 10

5 × 1 = 5
5 × 2 = 10
5 × 3 = 15
5 × 4 = 20
5 × 5 = 25
5 × 6 = 30
5 × 7 = 35
5 × 8 = 40
5 × 9 = 45
5 × 10 = 50
Program ran successfully. Exiting..
'''