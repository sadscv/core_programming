#! /usr/bin/env python

'''
this example is for os.path module
'''

import os
for tmpdir in ('/tmp', 'c:\temp'):
    if os.path.isdir(tmpdir):
        break
else:
    print('no temp directory available')

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print('****current temporary directory is :%s' % cwd)

    print('creating example directory')
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print('****new working directory is :%s' % cwd)
    print('****original directory listing :%s' % os.listdir(cwd))
    print('****creating test file')
    fobj = open('test', 'w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print('****updating directory listing: %s' % os.listdir(cwd))
    print('****renaming "test" to "filetest.txt"')
    os.rename('test', 'filetest.txt')
    print('****updating directory listing: %s' % os.listdir(cwd))

    path = os.path.join(cwd, os.listdir(cwd)[0])
    print('****full file pathname: %s' % path)
    print('****pathname basename: (%s, %s)' % (os.path.split(path)))
    print('****(filename, extension): %s')
    print(os.path.splitext(os.path.basename(path)))
    print('****displayin file contents: ')
    fobj = open(path)
    for line in fobj:
        print(line)
    fobj.close()

    print('***deleting test file')
    os.remove(path)
    print('****updating directory listing: %s' % os.listdir(cwd))
    os.chdir(os.pardir)
    print('***deleting test directory')
    os.rmdir('example')
    print('****done')
