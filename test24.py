#!/usr/bin/python
#-*-coding:utf-8-*-
#(24) (23)のプログラムを修正し，各トークンの末尾が記号で終わる場合は，その記号を別のトークンとして分離せよ

import sys
import re


#pattern = re.compile(r'[,?!.]$')
pattern = re.compile(r'\W$')

for line in sys.stdin:
	words = line.split(' ') #スペース区切りの単語を生成（記号は除去していない）
	i = 0
	for word in words:
		i += 1
		m = pattern.search(word)
		if m:
			print word[:m.start()]
			print word[m.start()]
			#if word[m.start()] == ".": #. の時空行
			#	print ""
		else:
			print word