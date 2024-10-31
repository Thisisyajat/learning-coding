# (C) Yajat Gupta
# Check if number is even or odd

n = int(input("Enter an integer number : "))
a = n % 2
if a == 0:
    print(n,"is even.")
elif a != 0:
    print(n,"is odd.")
