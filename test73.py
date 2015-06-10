#!/usr/bin/python
#-*-coding:utf-8-*-
#(73) 72のモジュールを用い，名詞句（NP）を抽出するプログラムを実装せよ．
#ただし，ひとつの名詞句の出現に対し，"# (名詞句)\n"という形式で出力せよ


import sys, os, os.path, pickle
from test72 import *


def main():
	texts = pickle.load(open("test72_texts.pkl","r"))

	NP = []

	for text in texts: #各テキスト
		for sent in text: #各文
			for morph in sent: #各morph
			
				if morph.chunk == "B-NP" : #名詞句のはじまり
					if NP != []:
						print "#"+" ".join(NP)
						NP=[]
					NP.append(morph.surface)
				elif morph.chunk == "I-NP": #名詞句の中間
					NP.append(morph.surface)
				else:
					if NP != []:
						print "#"+" ".join(NP)
						NP=[]

if __name__ == '__main__':
	main()

