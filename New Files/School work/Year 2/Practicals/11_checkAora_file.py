# A Python program to read a file named 'article.txt', count and print total words starting with “a” or “A” in the file.
# (C) Yajat Gupta

count = 0
line = ' '
with open(r'article.txt','r') as myfile:
    print('\nThe words are:')
    while line:
        line = myfile.readline()
        for word in line.split():
            if word[0] in ['a','A'] :
                count += 1
                print(word, end=' ')
    print(f'\nTotal number of words starting with a or A : {count}')
print('Program ran successfully. Exiting...')

# Output
'''

The words are:
amet, adipiscing aliqua. ad aliquip aute 
Total number of words starting with a or A : 6
Program ran successfully. Exiting...
'''