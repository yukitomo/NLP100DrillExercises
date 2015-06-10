#!/usr/bin/python
#-*-coding:utf-8-*-
#(23)(22)の出力を標準入力から１行（１文）を読み込む毎に，スペースで単語列に分割し，１行１単語形式で標準出力に書き出せ．文の終端を表すため，文が終わる毎に空行を出力せよ

import sys
import re

#sents=open(sys.argv[1])

for line in sys.stdin:
	words = line.split(' ') #スペース区切りの単語を生成（記号は除去していない）
	for word in words:
		print word
