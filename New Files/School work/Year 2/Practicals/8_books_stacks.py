# This python program to maintain book details like book code, book title and price using stacks data structures? (implement push(), pop() and traverse() functions).
# (C) Yajat Gupta

def push():
    code = int(input('\nEnter book code : '))
    title = input('Enter book title : ')
    price  = float(input('Enter book price : Rs. '))
    book = (code,title,price)
    books.append(book)
    print('\nValues pushed successfully.')

def pop():
    if len(books) == 0:
        print('\nUnderflow. No entries left to delete.')
    else:
        books.pop()
        print("Deleted the latest entry.")

def traverse():
    print()
    for i in range(len(books)-1, -1, -1):
        print(books[i])

books = []
condition = True
while condition:
    print(
        '''
        This program supports three functions for book management:
            '1'. Push (book code, book title, and book price)
            '2'. Pop (delete the latest entry)
            '3'. Traverse (show all the entries stored)
           To exit the program, type '4'. 
           Only numeric characters allowed.

 '''
    )
    mode = int(input('Please select your choice ==> '))
    if mode not in [1,2,3,4]:
        print('\nInvalid choice. Please try again.')
        continue
    else:
        if mode == 1:
            push()
            continue
        elif mode == 2:
            pop()
            continue
        elif mode == 3:
            traverse()
            continue
        elif mode == 4:
            condition = False
print('Program ran successfully. Exiting...')

# Output
'''
        This program supports three functions for book management:
            '1'. Push (book code, book title, and book price)
            '2'. Pop (delete the latest entry)
            '3'. Traverse (show all the entries stored)
           To exit the program, type '4'. 
           Only numeric characters allowed.

           
Please select your choice ==> 1

Enter book code : 101
Enter book title : The Alchemist
Enter book price : Rs. 250

Values pushed successfully.
    
            This program supports three functions for book management:
                '1'. Push (book code, book title, and book price)
                '2'. Pop (delete the latest entry)
                '3'. Traverse (show all the entries stored)
            To exit the program, type '4'. 
            Only numeric characters allowed.

Please select your choice ==> 1

Enter book code : 102
Enter book title : The Monk Who Sold His Ferrari
Enter book price : Rs. 300

Values pushed successfully.

            This program supports three functions for book management:
                '1'. Push (book code, book title, and book price)
                '2'. Pop (delete the latest entry)
                '3'. Traverse (show all the entries stored)
            To exit the program, type '4'.
            Only numeric characters allowed.

Please select your choice ==> 3
    
    (102, 'The Monk Who Sold His Ferrari', 300.0)
    (101, 'The Alchemist', 250.0)
    
                This program supports three functions for book management:
                    '1'. Push (book code, book title, and book price)
                    '2'. Pop (delete the latest entry)
                    '3'. Traverse (show all the entries stored)
                To exit the program, type '4'. 
                Only numeric characters allowed.

Please select your choice ==> 2
Deleted the latest entry.
    
                This program supports three functions for book management:
                    '1'. Push (book code, book title, and book price)
                    '2'. Pop (delete the latest entry)
                    '3'. Traverse (show all the entries stored)
                To exit the program, type '4'. 
                Only numeric characters allowed.

Please select your choice ==> 3
    
        (101, 'The Alchemist', 250.0)
        
                    This program supports three functions for book management:
                        '1'. Push (book code, book title, and book price)
                        '2'. Pop (delete the latest entry)
                        '3'. Traverse (show all the entries stored)
                    To exit the program, type '4'. 
                    Only numeric characters allowed.

Please select your choice ==> 4

Program ran successfully. Exiting...
'''