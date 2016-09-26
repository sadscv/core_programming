#! /usr/bin/env python

stack = []
# CMDs = {'u':push, 'o':pop, 'v':viewstack}

def push():
    stack.append(input('Enter New String:').strip())

def pop():
    if len(stack) <= 0:
        return('stack is empty')
    else:
        print('Removed %s' % stack.pop())

def viewstack():
    print(stack)

def showmenu():
    pr = '''
    p(U)sh
    p(O)p
    (V)iew
    (Q)uit

    Please Enter choice:
    '''
    while True:
        while True:
            try:
                choice = input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'

            print('You picked:[%s]' % choice)
            if choice not in 'uovq':
                print('invalid option, try again')
            else:
                break
        if choice == 'q':
            break
        if choice == 'u':
            push()
        if choice == 'o':
            pop()
        if choice == 'v':
            viewstack()



if __name__ == '__main__':
    showmenu()