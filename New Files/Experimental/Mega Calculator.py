# (C) Yajat Gupta
# WIP
# The program is a calculator with many mathematical operators. It only supports two numbers at a time.
# The program is in beta stage and is not complete yet. It is not recommended to use this program for any serious work.

print("Welcome to the Calculator.")
print("This program supports operations on only two numbers at a time.")
print("")
mode = input(
    """Select the arithmetic operation mode:
        1. Addition (type: add or +)
        2. Subtraction (type: sub or -)
        3. Multiplication (type: multiply or *)
        4. Division (type: div or /)
        5. Floor (type: floor)
        6. Modulo (type: mod or %)
        7. Factorial (type: fact or !)
        8. Power of a number (type : pow or **)
        ------------------------------------------
        9. Other applications (BETA) (type: other)
        ------------------------------------------
        
        Enter your response ---> """)
print("")
print("")

if mode == "add" or '+':
    a = float(input("Enter the first number --> "))
    b = float(input("Enter the second number --> "))
    print(f("{a} + {b} = {a + b}"))
    print("Program ran successfully. Restart to use again.")
elif mode == "sub" or '-':
    a = float(input("Enter the first number --> "))
    b = float(input("Enter the second number --> "))
    print(f("{a} - {b} = {a - b}"))
    print("Program ran successfully. Restart to use again.")
elif mode == "multiply" or '*':
    a = float(input("Enter the first number --> "))
    b = float(input("Enter the second number --> "))
    print(f("{a} * {b} = {a * b}"))
    print("Program ran successfully. Restart to use again.")
elif mode == "div" or '/':
    a = float(input("Enter the first number --> "))
    b = float(input("Enter the second number --> "))
    print(f("{a} / {b} = {a / b}"))
    print("Program ran successfully. Restart to use again.")
elif mode == "floor":
    a = float(input("Enter the first number --> "))
    b = float(input("Enter the second number --> "))
    print("Floor of the given numbers is:",a // b)
    print("Program ran successfully. Restart to use again.")
elif mode == "mod" or '%':
    a = float(input("Enter the first number --> "))
    b = float(input("Enter the second number --> "))
    print("Modulo of the given numbers is:",a % b)
    print("Program ran successfully. Restart to use again.")
elif mode == "fact" or '!':
    n = int(input("Enter an integer --> "))
    a = n
    fact = 1
    
    while (n >= 1):
        fact = fact * n
        n -= 1
    print("The factorial of",a,"is",fact,".")
    print("Program ran successfully. Restart to use again.")
elif mode == "pow" or '**':
    b = float(input("Enter the base number --> "))
    exp = float(input("Enter the exponent --> "))
    print(b,"^",exp," = ", b**exp)
    print("Program ran successfully. Restart to use again.")
elif mode == "other":
    mode2 = input('''Please select from the following options:
              1. Table of given number (type: table)

              Enter your response --> ''')
    if (mode2 == "table"):
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
            print("Program ran successfully. Restart to use again.")
    
else: print("Invalid input. Restart the program.")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# WIP
# The program is a calculator with many mathematical operators. It only supports two numbers at a time.
# The program is in beta stage and is not complete yet. It is not recommended to use this program for any serious work.
