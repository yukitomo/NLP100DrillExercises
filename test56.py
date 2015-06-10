#!/usr/bin/python
#-*-coding:utf-8-*-
#2014-12-14 Yuki Tomo
#(56) 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
#cat test51_japanese.txt|python test56.py

import sys
from test52 import Morph
from test53 import Chunk,cabtxt2chunk_inputter
from collections import defaultdict

def show_dependency_noun_verb(text):
	for i in range(len(text)):
		for j in range(len(text[i])):
			dst = text[i][j].dst
			if not dst == -1 :
				#係り元文節 text[i][j]
				#係り先文節 text[i][dst]
				if text[i][j].noun_in() and text[i][dst].verb_in(): #それぞれ名詞、動詞を含むか
					print "%s\t%s"%(text[i][j].phrase(), text[i][dst].phrase())		
			else:
				pass

def main():
	text_chunk = cabtxt2chunk_inputter(sys.stdin)
	show_dependency_noun_verb(text_chunk)

if __name__ == '__main__':
	main()