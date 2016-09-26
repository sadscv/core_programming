#! /usr/bin/env python

'''decorator demo'''
from time import time

option = {
    'pre' : 'pre_logged',
    'post' : 'post_logged'
}

def logged(when):
    def log(f, *args, **kargs):
        print('''Called:
        function: %s
        args: %r
        kargs: %r
        ''' % (f, args, kargs))

    def pre_logged(f):
        def wrapper(*args, **kargs):
            log(f, *args, **kargs)
            return f(*args, **kargs)
        return wrapper

    def post_logged(f):
        def wrapper(*args, **kargs):
            now = time()
            try:
                return f(*args, **kargs)
            finally:
                log(f, *args)
                print('time delta: %s' % (time()-now))
            return f(*args, **kargs)
        return wrapper

    try:
        choice = option[when]
    except KeyError as e:
        raise ValueError(e)

    if choice == 'pre_logged':
        return eval(choice)
    elif choice == 'post_logged':
        return vars()[choice]()
        # return eval(choice)



@logged('post')
def hello(name):
    print('hello, %s' % name)

hello('world!')