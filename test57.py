#!/usr/bin/python
#-*-coding:utf-8-*-
#2014-12-14 Yuki Tomo
#(57) (56)を修正し，非自立語は出力に含めないようにせよ
#cat test51_japanese.txt|python test57.py

import sys
from test52 import Morph
from test53 import Chunk,cabtxt2chunk_inputter
from collections import defaultdict

def show_dependency_indynoun_verb(text):
	for i in range(len(text)):
		for j in range(len(text[i])):
			dst = text[i][j].dst
			if not dst == -1 :
				#係り元文節 text[i][j]
				#係り先文節 text[i][dst]
				if text[i][j].noun_in() and text[i][dst].verb_in(): #それぞれ名詞、動詞を含むか
					#非自立語は除去
					print "%s\t%s"%(text[i][j].phrase_independent(), text[i][dst].phrase_independent())	
			else:
				pass

def main():
	text_chunk = cabtxt2chunk_inputter(sys.stdin)
	show_dependency_indynoun_verb(text_chunk)

if __name__ == '__main__':
	main()