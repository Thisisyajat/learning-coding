# (C) Yajat Gupta
# Prints a table of a given number using for loop

print("This program prints the table of given number.")
print()
n = int(input("Enter an integer --> "))
m = int(input("Enter a whole number of multiples to be printed --> "))
print()

if (m < 0):
    print("Number of multiples cannot be negative. Please rerun the program to continue.")
else:
    m += 1
    for i in range(1, m, 1):
        print(n, "X", i, "=", n * i)
        print()
    print("Program ran successfully.")
