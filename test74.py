#!/usr/bin/python
#-*-coding:utf-8-*-
#(74) 73で作成したプログラムを改変し，名詞句の冠詞が不定冠詞の場合は"A"，定冠詞の場合は"THE"，無冠詞の場合は"NONE"と表示するプログラムを実装せよ．
#ただし，73の表示内容に追加し，"# (名詞句)\n(冠詞タイプ)\n"という出力形式にせよ．

import sys, os, os.path
from test72 import *


if __name__ == "__main__":
	NP=[] #名詞句
	NPs=[] #名詞句のリスト
	texts_NPs=[] #各テキストの名詞句のリストのリスト
	texts = pickle.load(open("test72_texts.pkl","r"))

	for text in texts:
		for sent in text: #各文
			for morph in sent: #各morph
			
				if morph.chunk == "B-NP" : #名詞句のはじまり
					if NP != []:
						NPs.append(NP) 
						NP=[]
					NP.append(morph) #名詞句の始まりだった場合はmorphを格納
				elif morph.chunk == "I-NP": #名詞句の中間
					NP.append(morph) #名詞句の中間だったらmorphを格納
				else:
					if NP != []:
						NPs.append(NP)
						NP=[] #名詞句を初期化
		texts_NPs.append(NPs)

	for NPs in texts_NPs:
		for NP in NPs: #NP=[previous_morph,morph,morph,morph....]
			head = NP[0].surface.upper() #インデックスからが名詞
			if not head in ["A","AN","THE"]:
				head = "NONE"
			word=[]
			print "#"+" ".join([morph.surface for morph in NP[0:]]) #NPの名詞句の塊をプリント
			print head 
				
