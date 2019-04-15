#!/usr/bin/python
import sys

fname = sys.argv[1]
word_number = int(sys.argv[2])

f = open(fname, 'r')
text = f.read()
f.close()

words = text.replace('.', ' ').replace(',', ' ').split()

dic = dict()
for word in words:
    if word in dic:
        dic[word] = dic[word]+1
    else:
        dic[word] = 1

sorted_x = sorted(dic, key=dic.get, reverse=True)
sorted_list = [(key, dic[key]) for key in sorted_x]

for n in range(0, word_number):
    i, j = sorted_list[n]
    print '%-10s %10d'%(i, j)


