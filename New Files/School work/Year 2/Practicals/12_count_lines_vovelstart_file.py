# A Python program to read a file named “article.txt”, count and print total lines starting with vowels in the file.
# (C) Yajat Gupta

count = 0
line = ' '
with open(r'article.txt','r') as myfile:
    while line:
        line = myfile.readline()
        try:
            ch = line[0]
        except IndexError:
            pass
        if ch.lower() in ['a','e','i','o','u']:
            count += 1
    print(f'\nTotal number of lines starting with a vovel: {count}')
print('Program ran successfully. Exiting...')

# Output
'''

Total number of lines starting with a vovel: 2
Program ran successfully. Exiting...
'''