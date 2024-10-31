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

# Output
'''

Lorem#ipsum#dolor#sit#amet,#consectetur#adipiscing#elit.#Sed#do#eiusmod#tempor#incididunt#ut#labore#et#dolore#magna#aliqua.#95#Ut#enim#ad#minim#veniam,#quis#nostrud#exercitation#ullamco#laboris#nisi#ut#aliquip#ex#ea#commodo#consequat.#46#Duis#aute#irure#dolor#in#reprehenderit#in#voluptate#velit#esse#cillum#dolore#eu#fugiat#nulla#pariatur.#

Program ran successfully. Exiting...
'''