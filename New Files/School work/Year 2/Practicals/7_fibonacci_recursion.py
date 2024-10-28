# This program displays the Fibonacci sequence (0,1,1,2,3,5,8,13,21...) using 'recursion' method.
# (C) Yajat Gupta
def fibo(n):
    if n == 0:                                # Handle the base case for n == 0
        return 0
    elif n == 1:                              # Handle the base case for n == 1
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print('''
This program prints the Fibonacci Sequence upto a number given by the user.
''')
mode = True

while mode:
    terms = int(input('Enter the number of the sequence elements to be printed : '))
    if terms < 1:
        print('Invalid input. Please enter a number greater than or equal to 1.')
    else:
        print('Sequence ==> ', end ='')
        for i in range(terms):
            print(fibo(i), end = ' ')
        mode = input('\nDo you want to run the program again? Y/N : ')
        if mode.lower() in ['y','yo','yeah','yes']:
            continue
        else:
            mode = False
            print('Exiting the program...')

