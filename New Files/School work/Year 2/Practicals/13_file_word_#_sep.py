# A Python program to read a text file line by line and display each word separated by a #
# (C) Yajat Gupta

line = ' '
print()
with open(r'article.txt','r') as myfile:
    while line:
        line = myfile.readline()
        for word in line.split():
            print(word, end='#')
print('\n\nProgram ran successfully. Exiting...')