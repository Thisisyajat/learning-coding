# multiplication table generator

for i in range(1,26):
    print()
    for j in range(1,26):
        if (i*j) < 100 and (i*j) >= 10:
            print(f'{i * j} ',end='  ')
        elif (i*j) < 10:
            print(f'{i * j}',end='    ')
        else:
            print(f'{i * j}',end='  ')