#(C) Yajat Gupta
# Area and perimeter of square and rectangle (separate)

mode = input("Enter mode: square (type s) or rectangle (type r) : ")

if (mode == "s"):
    a = float(input("Enter the side of the square (in cm) : "))
    print("The area of the square with side", a, "is =", a * a, "cm².")
    print("")
    print("The perimeter of the square is =", 4 * a, "cm.")
    print("Program ran successfully. Exiting.")
elif (mode == "r"):
    l = float(input("Enter the length of the rectangle (in cm) : "))
    b = float(input("Enter the breadth of the rectangle (in cm) : "))
    print("")
    print("The area of the square with dimensions", l, "X", b, "is =", l * b, "cm².")
    print("The perimeter of the rectangle is =", 2 * (l + b), "cm.")
    print("Program ran successfully. Exiting.")
else:
    print("Invaid input. Please restart the program.")
