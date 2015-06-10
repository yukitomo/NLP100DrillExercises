#!/usr/bin/python
#-*-coding:utf-8-*-
#(35) 辞書引きを行った結果，３つ以上のエントリが見つかったもののみを出力せよ

import sys,marshal
from test33 import dict_searcher
		
def main():
	dictionary = marshal.load(open("dictionary.dump","r"))
	for line in sys.stdin:
		words=line.split("\t")
		dict_result = dict_searcher(words[1],dictionary)
		if dict_result:
			if len(dict_result) > 2:
				print words[1]
				for item in dict_result:
					print str(item)
			else:pass

if __name__ == '__main__':
	main()