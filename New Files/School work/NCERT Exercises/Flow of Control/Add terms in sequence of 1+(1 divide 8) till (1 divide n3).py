
# Add 1 + (1/8) + (1/27) + (1/64) + ..... (1/n³) (n entered by user)
# NCERT EXERCISES

m = 1
add = 0

print('''
            The program will add the terms in the following series:

            1 ,(1/8) , (1/27) , (1/64) , ...... (1/n³)
''')
print()
n = int(input("Enter natural number for n ==> "))

# n check
if (n < 1):
    print(f"ERROR: {n} is not a natural number. Exiting.")

# loop
while (m <= n):
    add += (1/(m ** 3))
    m += 1
print()
print(f"The sum of the terms in the series will be {add}.")
print("Program ran successfully. Exiting.")
