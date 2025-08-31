
# Prints minimum and maximum number of the five numbers entered by the user.
# NCERT EXERCISE

n = float(input("Enter the first number ==> "))
mini, maxi = n, n

for i in range(2,6):
    n = float(input(f"Enter number {i} ==> "))
    if (n < mini):
        mini = n
    elif (n > maxi):
        maxi = n
print("The maximum value entered is ==>", maxi)
print("The minimum value entered is ==>", mini)
