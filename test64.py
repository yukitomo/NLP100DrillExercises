#!/usr/bin/python
#-*-coding:utf-8-*-
#(64) 63の結果を用い，TF*IDF値が高い名詞句トップ100のリストを作成せよ．
#このとき，数字を含む表現はトップ100のリストから除外せよ．

#cat test63_output.txt |python test64.py
#python test63.py | python test64.py

import sys
import re 

def main():
	noun_tfidf = {}
	pattern = re.compile(r'[0-9:^]')

	for line in sys.stdin:
		items = line.strip().split("\t") #名詞句,TF*IDF,TF,DF
		noun_tfidf[items[0]] = float(items[1])

	i = 1
	for k,v in sorted(noun_tfidf.items(), key=lambda x:x[1], reverse=True):
		if i < 101:	
			if not pattern.search(k): #数字を含む表現はトップ100のリストから除外
				print "%d\t%s\t%f"%(i,k,v)
				i += 1
			
if __name__ == '__main__':
	main()