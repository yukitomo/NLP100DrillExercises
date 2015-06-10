#!/usr/bin/python
#-*-coding:utf-8-*-
#(34) 辞書引きを行った結果，辞書に載っていなかった語のみを出力せよ．
#cat medline.txt.sent.tok.stem |python test34.py 


import sys,marshal
from test33 import dict_searcher

def main():
	dictionary = marshal.load(open("dictionary.dump","r"))
	for line in sys.stdin:
		words=line.split("\t")
		dict_result = dict_searcher(words[1],dictionary)
		if not dict_result:
			print words[1] 

if __name__ == '__main__':
	main()