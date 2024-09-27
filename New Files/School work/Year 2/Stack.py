# Stack Operations
# (C) Yajat Gupta

def push(val):
    stack.append(val)
    print('Push successful.\n')
    return
def Pop():
    if isEmpty(stack) == True:
        print('UNDERFLOW! Stack is empty. Cannot pop any element.')
        print('Operation failed.\n')
    else:
        stack.pop()
        print('Top element popped successfully.')
    return
def peek():
    if isEmpty(stack) == True:
        print('Stack is empty.')
    else:
        print(stack[-1])
    return
def isEmpty(val):
    if val == []:
        return True
    else:
        return False
def Display():
    if isEmpty(stack) == True:
        print('Stack is empty.')
    else:
        print(f'{stack[-1]}     <-- Top')
        for i in range(len(stack)-2, -1, -1):
            print(f'{stack[i]}')
    return
stack = []
print(
    '''This program performs stack operations.
    Please enter any one of the following commands:
    1. Push
    2. Pop
    3. Peek
    4. Empty (to check if stack is empty)
    5. Display stack
    5. Exit
    '''
)
run = True
while run:
    com = input(('Enter your command ==> '))
    com = com.strip()
    com = com.lower()
    if com == 'push':
        e = input('Enter element to be pushed ==> ')
        push(e)
    elif com == 'pop':
        Pop()
    elif com == 'peek':
        peek()
    elif com == 'empty':
        print(isEmpty(stack))
    elif com == 'display':
        Display()
    elif com == 'exit':
        run = False
    else:
        print('Invalid input, try again.\n')

print('\nGoodbye.')