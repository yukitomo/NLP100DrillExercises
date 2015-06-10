#!/usr/bin/python
#-*-coding:utf-8-*-
#(16)括弧表現のうち，括弧の内側がアルファベット大文字の文字列，括弧の左側が漢字の文字列のものを抽出せよ．このとき，括弧の左側の表現と括弧の内側の表現をタブ区切り形式で出力せよ．
#python test16.py tweets.txt 

import sys
import re

pattern = re.compile(r'([一-龠]+)(\([A-Z]+\))')
#pattern = re.compile(r'\([A-Z]+?\)')

for line in sys.stdin:
	match=pattern.search(line)
	if match:
		print match.group(1)+"	"+match.group(2)

#for line in sys.stdin:
#	line = line.decode("utf-8")
#	match=pattern.search(line)
#	if match:
#		print match.group(1)+"	"+match.group(2)