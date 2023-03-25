# Just a simple, basic calculator, made with Python.
#Calculator functions
def add(num1,num2):
  return num1 + num2

def subtract(num1,num2):
  return num1 - num2

def multiply(num1,num2):
  return num1 * num2

def divide(num1,num2):
  return num1 / num2

print("Hi there! Welcome to the Basic Calculator.")
print("(Made by Yajat)")
print("Currenly, I support only two numbers per operation.\nIf you want to perform another operation, please rerun the program.\n\n")
num1 = float(input("Enter the first number. ---> "))
print("Which operation do you want to perform? Type any one of the following:\n1. Type 'Add' or '+'\nType 'Subtract' or '-'\n3. Type 'Multiply' or '*'\n4. Type 'Divide' or '/'\n")
op = input("Your input ---> ")

#Conditions
if op.lower() == "add" or op == "+":
  num2 = float(input("Enter the second number. ---> "))
  print(f"Answer to the expression {num1} + {num2} is {add(num1,num2)}\n")
  print("Rerun the program to continue.")

elif op.lower() == "subtract" or op == "-":
  num2 = float(input("Enter the second number. ---> "))
  print(f"Answer to the expression {num1} - {num2} is {subtract(num1,num2)}\n")
  print("Rerun the program to continue.")

elif op.lower() == "multiply" or op == "*":
  num2 = float(input("Enter the second number. ---> "))
  print(f"Answer to the expression {num1} * {num2} is {multiply(num1,num2)}\n")
  print("Rerun the program to continue.")

elif op.lower() == "divide" or op == "/":
  num2 = float(input("Enter the second number. ---> "))
  print(f"Answer to the expression {num1} / {num2} is {divide(num1,num2)}\n")
  print("Rerun the program to continue.")
else:
  print("You have entered an invalid operator. Please restart the program and try again.")
