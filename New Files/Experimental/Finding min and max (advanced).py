# EXPERIMENTAL
# FINDS MIN AND MAX OF ENTERED NUMBERS (CONTINUES TILL USER ENTERS 'end')
# Problem: floating points, negative numbers, exponential numbers i.e. numbers with symbols.

stop = False
min = max = float()

while stop == False :
    num = input("Enter the next number ==>  ")
    if num.isnumeric():
        num = float(num)
        if num > max:
            max = num
        elif num < min:
            min = num
    else:
        stop = True
        break
print(f"Minimum: {min}, Maximum: {max}")
