#! /usr/bin/env python3.5

'this is a function returning the type of a input'

def displayNumType(num):
    print('%s is' % num)
    if isinstance(num,(int, float, complex)):
        print('a number of type:', type(num).__name__)
    else:
        print('not a number at all')


displayNumType(-69)
displayNumType(9999999999999999999999999)
displayNumType(98.5)
displayNumType(-5.2+1.9j)
displayNumType('xxx')
