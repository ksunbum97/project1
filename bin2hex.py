#!/usr/bin/python

binum = input()
strbi = str(binum)
bilen = len(strbi)
dec = 0
decnum = 0
for i in range(0, bilen):
	if strbi[i] == "0":
		decnum = 0 * pow(2, i)
	elif strbi[i] == "1":
		decnum = 1 * pow(2, i)
	else:
		print("not binary number!")
	dec = dec + decnum
print "0X%X" % (dec)
	

