#!/usr/bin/python
#-*-coding:utf-8-*-
#2014-12-14 Yuki Tomo
#(55) 係り元の文節と係り先の文節をタブ区切り形式ですべて抽出せよ．
#ただし，句読点などの記号は出力しないようにせよ．

#係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）

#cat test51_japanese.txt|python test55.py

import sys
from test52 import Morph
from test53 import Chunk,cabtxt2chunk_inputter
from collections import defaultdict

def dependency_show(text):
	for i in range(len(text)):
		for j in range(len(text[i])):
			dst = text[i][j].dst 
			if not dst == -1:
				#係り元文節 text[i][j].show_phrase() 
				#係り先文節 text[i][dst].show_phrase() 
				print "%s\t%s"%(text[i][j].phrase(), text[i][dst].phrase())
			else:
				pass

def main():
	text_chunk = cabtxt2chunk_inputter(sys.stdin)
	dependency_show(text_chunk)

if __name__ == '__main__':
	main()