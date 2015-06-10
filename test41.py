#!/user/bin/python
#-*-coding:utf-8-*-
#(41) 日本語の文章をMeCabで形態素解析し，その結果を読み込むプログラムを実装せよ．
#ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
#１文は形態素（マッピング型）のリストとして表現せよ．
#python test41.py japanese.txt

import sys,MeCab,pickle

#text=[sentence1,sentence2,.....]
#sentence=[morpheme1,morpheme2,....]
#morpheme={"surface":表層系,"base":基本形,"pos":品詞,"pos1":品詞細分類１}
#text[m][n]["surface"]

def mecab_input(data):
	text=[]
	for line in open(data):
		tagger = MeCab.Tagger("mecabrc")
		line = tagger.parse(line).strip()
		print line
		words = line.split("\n")
		sentence = []
		for word in words:
			if not word == "EOS":
				word_items = word.split("\t")
				word_items2 = word_items[1].split(",")
				morpheme = {"surface":word_items[0],"base":word_items2[6],"pos":word_items2[0],"pos1":word_items2[1]}
				sentence.append(morpheme)
			else:
				text.append(sentence)
				sentence = []
	return text

def main():
	data_japanese=sys.argv[1]
	text=mecab_input(data_japanese)
	output_file = open("test41_output.pickle","w")
	pickle.dump(text,output_file)
	for line in text:
		for word in line:
			print "{surface:%s, base:%s, pos:%s, pos1:%s}" % (word["surface"],word["base"],word["pos"],word["pos1"])


if __name__ == '__main__':
	main()










