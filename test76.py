#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
import os, os.path
from test72 import *

def make_NPlearning_data(readfile,morph_text): #各テキスト
	write_file = open(readfile[:-9]+"f","w")
	NPs = input_NP_text(morph_text) #NPsに各NPを格納
	for NP in NPs:
		write_file.write(NP.showinfo(),)
		#print NP.showinfo(),
			
def main():
	for read_file in file_paths_getter('sec8_english_texts', '.genia'): #各geniaファイルのアドレスを取得
		#print readfile
		text = input_morph_txt(read_file) #geniaファイルからmorphのリストを作成
		make_NPlearning_data(read_file, text)


if __name__ == "__main__":
	main()


#77 学習 classias-train -tn -m model.txt  english.geniaf.txt english_2.geniaf.txt english_3.geniaf.txt english_4.geniaf.txt english_5.geniaf.txt
#78 cat english.geniaf.txt | classias-tag -m model.txt -r
#79 5分割交差検定 classias-train -tn -g5 -x english.geniaf.txt english_2.geniaf.txt english_3.geniaf.txt english_4.geniaf.txt english_5.geniaf.txt