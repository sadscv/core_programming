#! /usr/bin/env python

db = {}

def newuser():
    prompt = 'login desired:'
    while True:
        name = input(prompt)
        if name in db:
            prompt = 'name taken, please try another'
            continue
        else:
            break
    pwd = input('password:')
    db[name] = pwd


def olduser():
    name = input('username:')
    pwd = input('password:')
    password = db.get(name)
    if password == pwd:
        print('welcome back, %s' % name)
    else:
        print('login error,try again')

def showmenu():

    prompt = '''
    (N)ew User login
    (O)ld User Login
    (Q)uit
    Enter choice:
    '''

    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\n You Picked: [%s]' % choice)
            if choice not in 'noq':
                print('invalid options, try again')
            else:
                chosen = True

        if choice == 'q':
            done = True
        if choice == 'n':
            newuser()
        if choice == 'o':
            olduser()

if __name__ == '__main__':
    showmenu()