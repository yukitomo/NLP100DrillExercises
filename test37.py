#!/usr/bin/python
#-*-coding:utf-8-*-
#(37) (36)の出力を読み込み，単語の連接の頻度を求めよ．ただし，出力形式は"(連接の頻度)\t(現在の単語)\t(次の単語)"とせよ．
#cat medline.txt.sent.tok | python test36.py |python test37.py

import sys
from collections import defaultdict

def main():
	bigram_counts=defaultdict(int)
	for line in sys.stdin:
		bigram = line.strip()
		bigram_counts[bigram] += 1
	for k,v in bigram_counts.items():
		print "%d\t%s"%(v,k)

if __name__ == '__main__':
	main()