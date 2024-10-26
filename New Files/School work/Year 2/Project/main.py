import random
print("You will be awarded +10 for every correct guess and -3 for every wrong guess. Total 7 chances will be provided!.")
ans = 'Y'
while ans == 'Y':
    a = input('''
Choose a theme:-
        1. FRUITS
        2. TRANSPORT
        3. FLOWERS
        4. INDOOR GAMES
Enter the respective theme number: ''')
    if a not in ['1','2','3','4']:
        print('Invalid input! Try Again...')
    else:
        dash_count = 0
        name = input("Enter Player Name: ")
        print(name, 'let the game begin...!')
        score = 0
        chance = 7