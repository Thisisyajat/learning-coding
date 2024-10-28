# a random number generator that generates random numbers between  1 and 6 (simulate a dice).
# (C) Yajat Gupta
import random
print('This program throws a dice, and returns the number on it.')
mode = True
while mode:
    ans = input('Do you want to throw a dice? y/n : ')
    if ans.lower() in ['y','yes']:
        print(f'The number on the dice is ==> {random.randint(1,6)}\n')
    elif ans.lower() in ['n','no']:
        mode = False
        print('Program exiting...')
    else:
        print('Invalid choice. Please try again.\n')
