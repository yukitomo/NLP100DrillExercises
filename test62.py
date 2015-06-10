#!/usr/bin/python
#-*-coding:utf-8-*-
#(62)61で作成した各ファイルから，名詞句（文節中の名詞の連接）を抜き出して，個別のファイルに格納せよ．
#python test62.py

import sys, os, os.path, pickle
from collections import defaultdict
from test53 import *

def file_paths_getter(dir_path, extension):
	"""
	input : ディレクトリのパス、拡張子
	output : 各ファイルのパス
	"""
	extension_length = len(extension)
	for root,dirs,files in os.walk(dir_path):
		#print root,dirs,files
		paths=[]
		for file in files:
			file_address = os.path.join(root, file)
			if file_address[- extension_length :] == extension:
				#print file_address
				paths.append(file_address)
		return paths

def main():
	
	for read_file in file_paths_getter('work', '.txt'):
		print "reding " + read_file

		write_file = open(read_file+".n","w") #書き込みファイル名
		text = cabtxt2chunk_inputter(open(read_file,"r")) #chunkに格納
		pickle.dump(text, open(read_file+".pkl","w"))

		
		for i in range(len(text)): #はセンテンスの番号
			for j in range(len(text[i])): #はchunkの番号
				#各chunk中の名詞句(名詞の連接)をリストに格納して表示、ない場合は空のリスト[]となる 
				phrases = text[i][j].get_noun_phrases()

				"""				
				if text[i][j].noun_in():
					text[i][j].showinfo()
				"""

				#リストが空[]の場合は range(len(phrases)) = [] になるのでループは発生しない
				for k in range(len(phrases)):
					print phrases[k]
					write_file.write(phrases[k].strip()+"\n")
				



if __name__ == "__main__":
	main()


