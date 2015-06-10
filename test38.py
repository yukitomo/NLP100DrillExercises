#!/usr/bin/python
#-*-coding:utf-8-*-
#(38) (37)の出力を読み込み，ある単語wに続く単語zの条件付き確率P(z|w)を求めよ．ただし，出力形式は"(条件付き確率)\t(現在の単語)\t(次の単語)"とせよ．
#cat medline.txt.sent.tok | python test36.py |python test37.py |python test38.py

import sys
from collections import defaultdict

def probability(pre_count,next_count):
	return next_count/pre_count

def main():
	unigram_counts = defaultdict(int)
	bigram_counts =  defaultdict(lambda : defaultdict(int))

	for line in sys.stdin:
		[count,pre,next] = line.strip().split("\t")
		unigram_counts[pre] += float(count)
		bigram_counts[pre][next] += float(count)

	for w,w_c in unigram_counts.items():
		for z,z_c in bigram_counts[w].items():
			#print w_c, z_c
			#print probability(w_c, z_c)
			print "%f\t%s\t%s" % (probability(w_c, z_c), w, z) 

if __name__ == '__main__':
	main()
