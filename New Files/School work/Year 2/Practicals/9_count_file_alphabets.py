# A Python program to read a file named “article.txt”, count and print total alphabets in the file.
# (C) Yajat Gupta
count = 0
with open(r'article.txt','r') as myfile:
    text = myfile.read()
    for ch in text:
        if ch.isalpha() == True:
            count += 1
    print(f'\nTotal number of alphabets in the file: {count}')
print('Program ran successfully. Exiting...')
