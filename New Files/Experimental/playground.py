# Test file (playgroud)
# Content will be added soon.
# (C) Yajat Gupta
# WIP
# The program is a calculator with many mathematical operators. It only supports two numbers at a time.
# The program is in beta stage and is not complete yet. It is not recommended to use this program for any serious work.
def select(mode):
    operations = {
        "add": lambda a, b: a + b,
        "sub": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
        "div": lambda a, b: a / b,
        "floor": lambda a, b: a // b,
        "mod": lambda a, b: a % b,
        "fact": lambda n: factorial(n),
        "pow": lambda b, exp: b ** exp,
        "other": handle_other
    }

    if mode in operations:
        operation = operations[mode]
        operation_args = get_operation_args(mode)
        result = operation(*operation_args)
        print("Program ran successfully. Restart to use again.")
    else:
        print("Invalid input. Restart the program.")

def get_operation_args(mode):
    if mode in ["add", "sub", "multiply", "div", "floor", "mod"]:
        a = float(input("Enter the first number --> "))
        b = float(input("Enter the second number --> "))
        return (a, b)
    elif mode == "fact":
        n = int(input("Enter an integer --> "))
        return (n,)
    elif mode == "pow":
        b = float(input("Enter the base number --> "))
        exp = float(input("Enter the exponent --> "))
        return (b, exp)

def handle_other():
    mode2 = input('''Please select from the following options:
                  1. Table of given number (type: table)

                  Enter your response --> ''')
    if mode2 == "table":
        n = int(input("Enter an integer --> "))
        m = int(input("Enter a whole number of multiples to be printed --> "))
        print()

        if m < 0:
            print("Number of multiples cannot be negative. Please rerun the program to continue.")
        else:
            m += 1
            for i in range(1, m, 1):
                print(n, "X", i, "=", n * i)
                print()
            print("Program ran successfully. Restart to use again.")

def factorial(n):
    a = n
    fact = 1

    while n >= 1:
        fact = fact * n
        n -= 1

    print("The factorial of", a, "is", fact, ".")

print("Welcome to the Calculator.")
print("This program supports operations on only two numbers at a time.")
print("")
mode = input(
    """Select the arithmetic operation mode:
        1. Addition (type: add)
        2. Subtraction (type: sub)
        3. Multiplication (type: multiply)
        4. Division (type: div)
        5. Floor (type: floor)
        6. Modulo (type: mod)
        7. Factorial (type: fact)
        8. Power of a number (type : pow)
        ------------------------------------------
        9. Other applications (BETA) (type: other)
        ------------------------------------------
        
        Enter your response ---> """)
print("")
print("")
select(mode)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# WIP
# The program is a calculator with many mathematical operators. It only supports two numbers at a time.
# The program is in beta stage and is not complete yet. It is not recommended to use this program for any serious work.
#The main function, select, takes a string argument mode which specifies the operation to perform. It uses a dictionary named operations to map these operation names to their corresponding functions. These functions are mostly defined using lambda expressions for basic arithmetic operations such as addition, subtraction, multiplication, division (both floating-point and floor), modulus, and exponentiation. For factorial calculation and handling other unspecified operations, it refers to separate functions factorial and handle_other, respectively.
#The select function checks if the provided mode exists in the operations dictionary. If it does, it retrieves the corresponding operation function and calls get_operation_args to prompt the user for the necessary input arguments. These arguments are then passed to the operation function, and the result is calculated. If the mode is not recognized, it prints an error message.
#
#The get_operation_args function prompts the user for input based on the operation mode. For binary operations like addition or subtraction, it asks for two numbers. For the factorial operation, it requests a single integer, and for exponentiation, it asks for a base and an exponent. The inputs are converted to the appropriate types (float or int) before being returned.
#The handle_other function provides an additional layer of functionality by allowing the user to select from other non-standard operations, such as printing a multiplication table for a given number. It prompts the user for further input to specify the operation and executes it accordingly, including error handling for invalid inputs.
#
#Lastly, the factorial function calculates the factorial of a given number using a while loop. It iteratively multiplies the numbers from the given integer down to 1, printing the result at the end.

#This code demonstrates the use of dictionaries as a method for mapping strings to functions, lambda expressions for concise function definitions, input handling, and basic control flow with conditionals and loops. It's a practical example of how to build a simple, interactive command-line application in Python.