#!/usr/bin/python
#-*-coding:utf-8-*-
#(75) 74で作成したプログラムを改変し，以下の11種類の素性を抽出・表示するプログラムを実装せよ．
#ただし，これらの素性はタブ区切り形式で"# (名詞句)\n(冠詞タイプ)\t(タブ区切り形式の素性)\n"という形式で出力せよ．
#例えば，"A major challenge is [the limited number] of NOE restraints ..."の[]の部分の名詞句に対して，次の出力を得る（ただし"\"は実際にはここで改行しないことを表す） 

import sys
import os, os.path
from test72 import *

if __name__ == "__main__":

	for read_file in file_paths_getter('sec8_english_texts', '.genia'): #各geniaファイルのアドレスを取得
		#print readfile
		text = input_morph_txt(read_file) #geniaファイルからmorphのリストを作成
		NPs = input_NP_text(text) #morphのリストから名詞句のリストを作成
		for NP in NPs:
			print NP.showinfo(),