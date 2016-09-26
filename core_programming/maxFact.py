#! /usr/bin/env python

def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print('max factor of %d is %d' % (num ,count))
            break
        else:
            count -= 1
    else:
        print('%d is prime' % num)

for i in range(10, 21):
    showMaxFactor(i)