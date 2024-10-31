#   Write a python program to read a file named “article.txt”, count and print the following: 
#         (i) length of the file(total characters in file) 
#         (ii) total alphabets 
#         (iii) total upper case alphabets 
#         (iv) total lower case alphabets 
#         (v) total digits 
#         (vi) total spaces 
#         (vii) total special characters
# (C) Yajat Gupta

length = alpha = upalpha = lowalpha = digits = spaces = spch = 0
with open(r'article.txt','r') as myfile:
    text = myfile.read()
    length = len(text)
    for ch in text:
        if ch.isalpha() == True:
            alpha += 1
            if ch.isupper() == True:
                upalpha += 1
            elif ch.islower() == True:
                lowalpha += 1
        elif ch.isdigit() == True:
            digits += 1
        elif ch == ' ':
            spaces += 1
        else:
            spch += 1
    print(f'''
          Analysis:
            1. Length of text       : {length}
            2. Alphabets            : {alpha}
            3. Upper-case alphabets : {upalpha}
            4. Lower-case alphabets : {lowalpha}
            5. Digits               : {digits}
            6. Spaces               : {spaces}
            7. Special characters   : {spch}

''')
print('Program ran successfully. Exiting...')

# Output
'''
          Analysis:
            1. Length of text       : 343
            2. Alphabets            : 277
            3. Upper-case alphabets : 4
            4. Lower-case alphabets : 273
            5. Digits               : 4
            6. Spaces               : 53
            7. Special characters   : 9


Program ran successfully. Exiting...
'''