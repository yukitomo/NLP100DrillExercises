#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from test10 import *
bigram=[]

for line in open(sys.argv[1]):
	line=line.lower().strip()
	if len(line) > 1:
		for a in range(len(line)-1):
			bi=line[a:a+2]
			bigram.append(bi)

bigram_counts = word_counter(bigram)
top_n_order(bigram_counts,100)



