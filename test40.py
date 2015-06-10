#!/usr/bin/python
#-*-coding:utf-8-*-
#(40)(39)で構築したデータベースを読み込み，標準入力から読み込んだ文の生起確率を計算せよ.
#入力された文が単語列(w1, w2, ..., wN)で構成されるとき，生起確率はP(w2|w1)P(w3|w2)...P(wN|wN-1)と求めればよい．
#試しに，"this paper is organized as follows"と"is this paper organized as follows"の生起確率を計算せよ．

import kyotocabinet as kc
import sys
from test39 import KyotoCabinet

def get_sent_probability(db,sent):
	probability = 1
	for i in range(len(sent)-1):
		prob = db.get_str((sent[i], sent[i+1]))
		#print prob
		if not prob:
			prob = 0
		probability = float(prob) * probability
	return probability

def main():
    db = KyotoCabinet()
    db.open("test39_db.kch", kc.DB.OWRITER | kc.DB.OCREATE)

    sent = raw_input('input a sentence\n')
    sent = sent.strip().split()
    probability = get_sent_probability(db, sent)
    print probability

if __name__ == '__main__':
	main()