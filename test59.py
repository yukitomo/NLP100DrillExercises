#!/usr/bin/python
#-*-coding:utf-8-*-
#2014-12-14 Yuki Tomo
#(59) 各文に含まれるすべての体言（名詞を含む文節）の組み合わせに対し，その文節間の表現（係り受けパス）を出力せよ．
#cat test51_japanese.txt|python test59.py

import sys
from test52 import Morph
from test53 import Chunk,cabtxt2chunk_inputter
from collections import defaultdict

def noun_combi_path_show(text):
	for i in range(len(text)):
		for j in range(len(text[i])):
			dst = text[i][j].dst
			if not dst == -1 :
				if text[i][j].noun_in() and text[i][dst].noun_in():
					print "%s\t%s"%(text[i][j].phrase_independent(), text[i][dst].phrase_independent())
					print str(j)+" → "+str(dst)

def main():
	text_chunk = cabtxt2chunk_inputter(sys.stdin)
	noun_combi_path_show(text_chunk)
	
if __name__ == '__main__':
	main()