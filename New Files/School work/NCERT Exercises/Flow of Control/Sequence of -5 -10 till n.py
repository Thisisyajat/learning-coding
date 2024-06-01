
# Continue sequence -5, -10, -15,.... till n (entered by user)
# NCERT EXERCISES

a = 0
d = -5
m = 1

n = int(input("Enter a natural number 'n' to decide the number of terms in the sequence ==> "))

# n checks
if (n < 1):
    print(f"ERROR: {n} is not a natural number. Exiting.")

while m <= n:
    a += d
    print(a, end=" , ")
    m += 1
print()
print("Program ran successfully. Exiting.")
