#!/usr/bin/python
import re

var1 = raw_input("Please enter the first list: ")
var2 = raw_input("Please enter the second list: ")

count = 0

lenvar1 = len(var1)
lenvar2 = len(var2)

union = []
intersection = []
list1 = []
list2 = []
dellist= []

list1 = re.findall("\d+", var1)
list2 = re.findall("\d+", var2)

lenlist1 = len(list1)
lenlist2 = len(list2)

#print 'list1 ==> %s'%(list1)
#print 'list2 ==> %s'%(list2)

for i in range (0, lenlist1):
	union.append(int(list1[i]))
for i in range (0, lenlist2):
	if int(list2[i]) not in union:
		union.append(int(list2[i]))

for i in range (0, lenlist1):
	for j in range(0, lenlist2):
		if list1[i] == list2[j]:
			if int(list1[i]) not in intersection:
				  intersection.append(int(list1[i]))

print "union: ", union			

print "intersection: ", intersection

