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