#! /usr/bin/env python

import os

fname = 'test'
print(max(len(line.strip()) for line in open('test')))


# if os.path.exists(fname):
#     f = open(fname, 'r')
#     iter = (word for line in f for word in line.split())
#     sum = sum(len(word) for line in f for word in line.split())
#     # print(sum)




# rows = [1,2,3,4,5]
# def cols():
#     yield 56
#     yield 2
#     yield 3
#     yield 1
#
# result = [(x, y) for x in rows for y in cols()]
# print(result)

# for i in result:
#     print(i)