
# Check if number is palindrome
# NCERT EXERCISES

num = int(input("Enter a natural number: ")) #12321
nnum = num                          #12321
rev = 0

# n check:
if (num < 1):
    print("ERROR: Entered number is not a nautral number. Restart the program to continue.")

while (nnum != 0): #true
    digit = nnum % 10             #1, 2, 3 ...
    nnum = nnum // 10             #1232, 123, 12 ...
    rev = (rev * 10) + digit      #1,12, 123 ...
if rev == num:
    print(f"{num} is a palindrome.")
    print()
    print("Program ran successfully, exiting.")
else: print(f"{num} is not a palindrome.")
