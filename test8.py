#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
address=[]

for line in open(sys.argv[1]):
	itemList = line[:-1].split('	')
	address.append(itemList)
	
sorted(address, key=lambda col:col[1])

for n in range(len(address)):
	print address[n][0]+"	"+address[n][1]+"\n",


