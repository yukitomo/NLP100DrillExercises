#!/usr/bin/python
#-*-coding:utf-8-*-
#(72) 71の解析結果を読み込むモジュールを実装せよ．
#各トークンは表層形（w），レンマ（lem），品詞（pos），チャンクタグ（chunk）をキーとするマッピング型に格納し，
#１文はトークン（マッピング型）のリストとして表現せよ（固有表現情報は読み込まなくてもよい）．

import sys, os, os.path
from test62 import *


class Morph_english:
	def __init__(self,surface,lem,pos,chunk): 
		self.surface=surface
		self.lem=lem
		self.pos=pos
		self.chunk=chunk

	def showinfo(self):
		return self.surface+"\t"+self.lem+"\t"+self.pos+"\t"+self.chunk

def input_morph_txt(genia_txt): #genia_txtのアドレス
	text = []
	sent = []
	for line in open(genia_txt):
		line = line.strip()
		if line != "EOS": #文末でなければ
			word_items = line.split("\t")
			morph = Morph_english(word_items[0],word_items[1],word_items[2],word_items[3])
			sent.append(morph)
		else:
			text.append(sent)
			sent=[]
	return text


class NP_pre_nex:
	def __init__(self,NP,previous_morph,next_morph): #名詞句、前の単語、次の単語
		self.NP=NP
		self.previous=previous_morph
		self.next=next_morph
	def showinfo(self):
		head = self.NP[0].surface.upper() #冠詞タイプ(head)の取得
		s = 1 #冠詞があるときの名詞句の１単語目
		if not head in ["A","AN","THE"]:
				head = "NONE"
				s = 0 #冠詞がないときの名詞句の１単語め
		elif len(self.NP) == 1: #"A","AN","THE"が冠詞にあって名詞句がそれしかないとき
			self.NP.append(Morph_english("*","*","*","*"))
		else:pass

		string = head + " " + \
		"w[-1]=" + self.previous.surface + " " +\
		"fw=" + self.NP[s].surface + " " +\
		"fpos=" + self.NP[s].pos + " " + \
		"w[0]=" + "\t".join([morph.surface for morph in self.NP[s:]]) + " " +\
		"fw|fpos=" + self.NP[s].surface + "|" + self.NP[s].pos + " " +\
		"hw=" + self.NP[-1].surface + " " +\
		"hw|hpos=" + self.NP[-1].surface + "|" + self.NP[-1].pos + " " +\
		"pos[+1]=" + self.next.pos + " " +\
		"hpos=" + self.NP[-1].pos + " " +\
		"pos[-1]=" + self.previous.pos + " "+\
		"w[+1]=" + self.next.surface

		np = "#"+" ".join([morph.surface for morph in self.NP[0:]])
		return np +"\n" + string + "\n"


def input_NP_text(text):
	NP=[] #名詞句
	NPs=[] #名詞句のリスト
	for sent in text: #各文
		for morph in sent: #各morph
			if morph.chunk == "B-NP" : #名詞句のはじまり
				if NP != []:
					#NPs.append(NP)
					if sent.index(NP[0])-1 > 0:
						previous_morph = sent[sent.index(NP[0])-1] #名詞句の前の単語
					else:
						previous_morph = Morph_english("*","*","*","*") #前の単語がなければすべての要素にnoneを入れる
					if sent.index(NP[-1])+1 <= len(sent)-1:
						next_morph = sent[sent.index(NP[-1])+1] #名詞句の後の単語
					else:
						next_morph = Morph_english("*","*","*","*")  #次の単語がなければ
					NP_class = NP_pre_nex(NP,previous_morph,next_morph)
					NPs.append(NP_class) 
					NP=[]
					"""
					previous_word=sent[sent.index(morph)-1]
					NP.append(previous_word) #インデックス０に前の単語を格納
					NP.append(morph) #名詞句の始まりだった場合はmorphを格納
					"""
				NP.append(morph)
			elif morph.chunk == "I-NP": #名詞句の中間
				NP.append(morph) #名詞句の中間だったらmorphを格納
			else:
				if NP != []:
					if sent.index(NP[0])-1 > 0:
						previous_morph = sent[sent.index(NP[0])-1] #名詞句の前の単語
					else:
						previous_morph = Morph_english("*","*","*","*") 
					if sent.index(NP[-1])+1 <= len(sent)-1:
						next_morph = sent[sent.index(NP[-1])+1] #名詞句の後の単語
					else:
						next_morph = Morph_english("*","*","*","*") 
					NP_class = NP_pre_nex(NP,previous_morph,next_morph)
					NPs.append(NP_class) 
					NP=[]
	return NPs


	

"""
word1   base1   POStag1 chunktag1 NEtag1
word2   base2   POStag2 chunktag2 NEtag2

"""

def main():
	genia_file_paths = file_paths_getter('sec8_english_texts', '.genia')

	texts = []
	for read_file in genia_file_paths:
		texts.append(input_morph_txt(read_file))

	for text in texts:
		for sent in text:
			for morph in sent:
				print morph.showinfo()

	pickle.dump(texts, open("test72_texts.pkl","w"))





if __name__ == "__main__":
	main()			