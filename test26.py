#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import re

#tokens = open(sys.argv[1]) #output24.txt
pattern = re.compile(r'(ly|ness)$') 

for line in sys.stdin:
	if pattern.search(line):
		print line.strip()