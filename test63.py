#!/usr/bin/python
#-*-coding:utf-8-*-

#(63) 62の結果を用い，それぞれの名詞句のTF*IDF値を計算し，"(名詞句)\t(TF*IDF値)\t(TF値)\t(DF値)"の形式で出力せよ．
#ある名詞句wがあるとき，freq(w)をコーパス全体での名詞句wの出現頻度，df(w)を名詞句wが出現するファイルの数，Nを総ファイル数とし，TF*IDF値は freq(w) * log(N / df(w)) として計算せよ
#python test63.py

import sys, os, os.path
from collections import defaultdict
from test53 import *
from test62 import file_paths_getter
import math

def main():
	df = defaultdict(lambda :[])
	tf = defaultdict(lambda :0)
	noun_phrases_files = file_paths_getter("work", ".n")
	N = float(len(noun_phrases_files))
	
	for read_file in noun_phrases_files: #.nのつくファイルのパスのリスト
		#print read_file
		for noun_phrase in open(read_file,"r"):
			noun_phrase = noun_phrase.strip()
			tf[noun_phrase] += 1 #名詞句のコーパス中の総合出現回数

			if not read_file in df[noun_phrase]:
				df[noun_phrase].append(read_file)

	for word in df.keys():
		TF = float(tf[word])
		DF = len(df[word])
		TFIDF = TF * math.log(N / DF, 2)
		print "%s\t%f\t%f\t%f"%(word, TFIDF, TF, DF)


if __name__ == "__main__":
	main()

