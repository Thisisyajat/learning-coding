# Program to shift elements of a list to the left by a given number of positions.
# (C) Yajat Gupta

def LShift(lst, n):
    L = len(lst)
    for i in range(0, n): # Loop to shift elements n times
        y = lst[0] # Store the first element in a variable
        for j in range(0, L-1): # Loop to shift elements by one position
            lst[j] = lst[j + 1] # Shift elements by one position
        lst[L-1] = y # Assign the first element to the last position
    print(lst)

a = list(input("Enter the list: "))
n = int(input("Enter the number of positions to shift: "))
LShift(a,n)