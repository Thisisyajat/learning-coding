# (C) Yajat Gupta
# Factorial of given number.

print("This program is designed to calculate the factorial of the entered number.")
print("")

n = int(input("Enter an integer --> "))
a = n
fact = 1

while (n >= 1):
    fact *= n
    n -= 1
    
print("The factorial of", a, "is", fact, ".")
