#! /usr/bin/env python

'makeTextFile.py -- create text files'

import os
ls = os.linesep

while True:
    fname = input('please input file name')
    if os.path.exists(fname):
        print('Error: %s already exists' % fname)
    else:
        break

#get file content (text) lines
all = []
print ("\n Enter lines ('.' by itself to quit).\n")

# loop until user teminates input
while True:
    entry = input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print('DONE!')