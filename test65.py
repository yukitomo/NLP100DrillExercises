#!/usr/bin/python
#-*-coding:utf-8-*-

#(65) 64のリストに含まれる名詞句に対し，その名詞句に係る文節・その名詞句が係る文節の単語（周辺単語と呼ぶ）を出力するプログラムを実装せよ．
#周辺単語は名詞，動詞，形容詞の基本形とせよ．出力形式は，"(名詞句)\t(方向) (周辺単語)"とし，名詞句に係る文節では「方向」を"<-"とし，名詞句が係る文節では「方向」を"->"とせよ．以降，「方向」と「周辺単語」を組み合わせたものを，名詞句の「文脈」と呼ぶ．

#cat test64_output.txt | python test65.py

import sys, os, os.path, math, re
from collections import defaultdict
from test52 import *
from test53 import *
from test62 import *


def main():
	#test64の名詞句を格納
	top100_noun_phrases = [line.strip().split("\t")[1] for line in sys.stdin]

	#test62であらかじめcabochaにかけてchunkのlist in list にしたもののdumpをpklでload
	for read_file in file_paths_getter('work', '.pkl'):
		#print "reading : " + read_file 
		text =  pickle.load(open(read_file, "r"))

		for i in range(len(text)): #sentence_id
			for j in range(len(text[i])): #chunk_id in sentence
				nps = text[i][j].get_noun_phrases() #chunk中の名詞句を取得

				for np in nps: #名詞句のリストが空のときはループに入らない
					if np in top100_noun_phrases: #chunk中の名詞句npがtop100中にあれば係り受けを出力
						dst = text[i][j].dst
						srcs = text[i][j].srcs

						if not dst == -1:
							#係り先 dst の周辺単語をリストとして獲得
							dst_words = text[i][dst].get_around_words()
							for dst_word in dst_words:
								print "%s\t->\t%s"%(np, dst_word)

						for src in srcs:
							src_words = text[i][src].get_around_words()
							for src_word in src_words:
								print  "%s\t<-\t%s"%(np, src_word)

















if __name__ == '__main__':
	main()