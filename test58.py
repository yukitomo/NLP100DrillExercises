#!/usr/bin/python
#-*-coding:utf-8-*-
#2014-12-14 Yuki Tomo
#(58) 係り元が２つ以上ある文節に対し，その文節とすべての係り元を表示せよ．
#cat test51_japanese.txt|python test58.py


import sys
from test52 import Morph
from test53 import Chunk,cabtxt2chunk_inputter
from collections import defaultdict

def show_dependency_multi(text):
	for i in range(len(text)):
		for j in range(len(text[i])):
			srcs = text[i][j].srcs
			if len(srcs) > 1:
				phrase_depended = text[i][j].phrase() #係り先
				phrases_depend = [text[i][src].phrase() for src in srcs] #係り元のリスト
				
				print "--phrase_depend--"
				for phrase in phrases_depend:
					print phrase
				print "--phrases_depended--"			
				print phrase_depended
				print ""

def main():
	text_chunk = cabtxt2chunk_inputter(sys.stdin)
	show_dependency_multi(text_chunk)
	
if __name__ == '__main__':
	main()