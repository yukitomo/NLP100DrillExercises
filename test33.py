#!/usr/bin/python
#-*-coding:utf-8-*-
#(33) (32)で作成した辞書を読み込み，１行１単語形式（例えばmedline.txt.sent.tok.stem）で標準入力から読み込んだ単語に対して，辞書引き結果を付与するプログラムを実装せよ．
#cat medline.txt.sent.tok.stem |python test33.py 

import sys
import marshal

def dict_searcher(word,dictionary):
	if word in dictionary.keys():
		return dictionary[word]
	else:
		return None
		
def main():
	dictionary = marshal.load(open("dictionary.dump","r"))
	for line in sys.stdin:
		words=line.split("\t")
		dict_result = dict_searcher(words[1],dictionary)
		if dict_result:
			print words[1] 
			for item in dict_result:
				print str(item)
		else:pass

if __name__ == '__main__':
	main()