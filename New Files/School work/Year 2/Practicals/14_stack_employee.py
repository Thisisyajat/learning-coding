# This program implements a stack for the employee details (empno, name)
# (C) Yajat Gupta

def push():
    code = int(input('\nEnter employee code : '))
    title = input('Enter employee name : ')
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
    for i in range(len(employees)-1, -1, -1):
        print(employees[i])

employees = []
condition = True
while condition:
    print(
        '''
        This program supports three functions for employee management:
            '1'. Push (employee code, employee title)
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
print('Exiting...')