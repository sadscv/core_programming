#! /usr/bin/env python

stack = []
# CMDs = {'e':enQ, 'd':deQ, 'v':viewquery}

def enQ():
    stack.append(input('Enter New String:').strip())

def deQ():
    if len(stack) <= 0:
        return('stack is empty')
    else:
        print('Removed %s' % stack.pop(0))

def viewstack():
    print(stack)

def showmenu():
    pr = '''
    (E)nQ
    (D)eQ
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
            if choice not in 'edqv':
                print('invalid option, try again')
            else:
                break
        if choice == 'q':
            break
        if choice == 'e':
            enQ()
        if choice == 'd':
            deQ()
        if choice == 'v':
            viewstack()



if __name__ == '__main__':
    showmenu()