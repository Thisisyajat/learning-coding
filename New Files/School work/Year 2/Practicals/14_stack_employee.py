# This program implements a stack for the employee details (empno, name)
# (C) Yajat Gupta

def push():
    code = int(input('\nEnter employee code : '))
    name = input('Enter employee name : ')
    employee = (code,title)
    employees.append(employee)
    print('\nValues pushed successfully.')

def pop():
    if len(employees) == 0:
        print('\nUnderflow. No entries left to delete.')
    else:
        employees.pop()
        print("Deleted the latest entry.")

def traverse():
    print()
    if isEmpty(employees) == True:
        print('Stack is empty.')
    else:
        print(f'{employees[-1]}     <-- Top')
        for i in range(len(employees)-2, -1, -1):
            print(f'{employees[i]}')
    return

def peek():
    if isEmpty(employees) == True:
        print('Stack is empty.')
    else:
        print(employees[-1])
    return

def isEmpty(val):
    if val == []:
        return True
    else:
        return False
employees = []
condition = True
while condition:
    print(
        '''
        This program supports four functions for employee management:
            '1'. Push (employee code, employee name)
            '2'. Pop (delete the latest entry)
            '3'. Traverse (show all the entries stored)
            '4'. Peek (show the latest entry)
           To exit the program, type '5'. 
           Only numeric characters allowed.

 '''
    )
    mode = int(input('Please select your choice ==> '))
    if mode not in [1,2,3,4,5]:
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
            peek()
            continue
        elif mode == 5:
            condition = False
print('Program ran successfully. Exiting...')

# Output
'''
        This program supports three functions for employee management:
            '1'. Push (employee code, employee title)
            '2'. Pop (delete the latest entry)
            '3'. Traverse (show all the entries stored)
           To exit the program, type '4'. 
           Only numeric characters allowed.


Please select your choice ==> 1

Enter employee code : 101
Enter employee name : Yajat

Values pushed successfully.
    
            This program supports three functions for employee management:
                '1'. Push (employee code, employee title)
                '2'. Pop (delete the latest entry)
                '3'. Traverse (show all the entries stored)
            To exit the program, type '4'. 
            Only numeric characters allowed.


Please select your choice ==> 1

Enter employee code : 102
Enter employee name : Gupta

Values pushed successfully.
        
                This program supports three functions for employee management:
                    '1'. Push (employee code, employee title)
                    '2'. Pop (delete the latest entry)
                    '3'. Traverse (show all the entries stored)
                To exit the program, type '4'. 
                Only numeric characters allowed.


Please select your choice ==> 3
    
    (102, 'Gupta')
    (101, 'Yajat')
        
                    This program supports three functions for employee management:
                        '1'. Push (employee code, employee title)
                        '2'. Pop (delete the latest entry)
                        '3'. Traverse (show all the entries stored)
                    To exit the program, type '4'. 
                    Only numeric characters allowed.


Please select your choice ==> 2
Deleted the latest entry.

                        This program supports three functions for employee management:
                            '1'. Push (employee code, employee title)
                            '2'. Pop (delete the latest entry)
                            '3'. Traverse (show all the entries stored)
                        To exit the program, type '4'. 
                        Only numeric characters allowed.


Please select your choice ==> 3
    
        (101, 'Yajat')
            
                        This program supports three functions for employee management:
                            '1'. Push (employee code, employee title)
                            '2'. Pop (delete the latest entry)
                            '3'. Traverse (show all the entries stored)
                        To exit the program, type '4'. 
                        Only numeric characters allowed.


Please select your choice ==> 4
Program ran successfully. Exiting...
'''
