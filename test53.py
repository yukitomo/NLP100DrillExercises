#!/usr/bin/python
#-*-coding:utf-8-*-
#(53) 文節を表すクラスChunkを実装せよ．このクラスは形態素のリスト（morphs），係り先文節インデックス番号（dst），
#係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，(51)の解析結果を１文毎に読み込み，
#１文をChunkオブジェクトのリストとして表現し，適当に表示するプログラムを実装せよ．

#cat test51_japanese.txt |python test52.py 

import sys
from test52 import Morph,object_printer,txtlist_opener
from collections import defaultdict

class Chunk:
	def __init__(self,morphs,dst,srcs): #chunk=Chunk(morphs,dst,src) dst:係り先文節インデックス番号 srcs:係り元文節インデックスリスト
		self.morphs = morphs
		self.dst = dst
		self.srcs = srcs

	def showinfo(self):
		for k in range(len(self.morphs)):
			if not self.morphs[k].showinfo() == None:
				print self.morphs[k].showinfo()
		print "dst=", self.dst, "srcs=", self.srcs
	
	def phrase(self):
		#1chunkのかたまりをreturn
		phrase=[]
		for k in range(len(self.morphs)):
			if self.morphs[k].pos != "記号":
				phrase.append(self.morphs[k].surface)
		return "".join(phrase)
	
	def noun_in(self):
		#対象のchunkが名詞をもつかTF値をreturn
		tf = False
		for k in range(len(self.morphs)):
			if self.morphs[k].pos == "名詞":
				tf=True
		return tf
	
	def verb_in(self):
		#対象のchunkが動詞をもつか
		tf = False
		for k in range(len(self.morphs)):
			if self.morphs[k].pos == "動詞":
				tf=True
		return tf
	
	def phrase_independent(self):
		#1chunkの非自立語は表示しない
		phrase=[]
		for k in range(len(self.morphs)):
			if self.morphs[k].pos != "記号" and self.morphs[k].pos1 != "非自立":
				phrase.append(self.morphs[k].surface)
		return "".join(phrase)
	
	def get_noun_phrases(self):
		#名詞句(名詞が1個以上連接)のリストを返す
		phrases = defaultdict(lambda :[])
		i = 0

		for k in range(len(self.morphs)):
			if self.morphs[k].pos == "名詞":
				phrases[i].append(self.morphs[k].surface)
			else: 
				i += 1

		noun_phrases = []
		for p in phrases.values():
			if len(p) > 0:
				phrase = "".join(p)
				noun_phrases.append(phrase)
		return noun_phrases
	
	def get_around_words(self):
		#周辺単語(名詞,動詞,形容詞)の基本形のリストを返す
		words=[]
		for k in range(len(self.morphs)):
			if self.morphs[k].pos == "動詞" or self.morphs[k].pos == "形容詞":
				words.append(self.morphs[k].base) #基本形
			elif self.morphs[k].pos == "名詞" :
				words.append(self.morphs[k].surface) #名詞はsurface
		return words

"""
--------------ja_caboha.txt--------------------       |
* 0 1D 0/1 0.000000                                   |chunk0 dst=1,srcs=[]
本編	名詞,一般,*,*,*,*,本編,ホンペン,ホンペン              | morph0
の	助詞,連体化,*,*,*,*,の,ノ,ノ                        | morph1 

* 1 -1D 3/3 0.000000                                   |chunk1 dst=None,srcs=[1]
主人公	名詞,一般,*,*,*,*,主人公,シュジンコウ,シュジンコー  |morph0
[	名詞,サ変接続,*,*,*,*,*                              |morph1
編集	名詞,サ変接続,*,*,*,*,編集,ヘンシュウ,ヘンシュー
]	名詞,サ変接続,*,*,*,*,*
EOS
"""

def cabtxt2chunk_inputter(data):
	text=[] #=[sent0,sent1.....]
	sent=[] #=[chunk0,chunk1,......] 各文節が入っている
	srcs_dict = defaultdict(lambda :[]) #={0:[],1:[0],....,ID:[3,4..]}
	morphs = []

	#for line in sys.stdin: #test51_japanese.txt
	for line in data: #test51_japanese.txt
		line = line.strip()
		if line[:2] == "* ":
			if len(morphs) != 0:
				chunk = Chunk(morphs,dst,srcs)
				sent.append(chunk)
				morphs = []
			info = line.strip().split()
			ID = int(info[1]) #chunkのID
			dst = int(info[2][:-1]) #Dの除去
			srcs_dict[dst].append(ID) #係り先のdstをキーとして、係りもととしてIDの値をアペンド
			srcs = srcs_dict[ID]
		elif not line == "EOS":
			word_items = line.split("\t") # word_items=["表層系","名詞,サ変接続,*,*,*,*,編集,ヘンシュウ,ヘンシュー"]
			word_items2 = word_items[1].split(",")
			morph = Morph(word_items[0],word_items2[6],word_items2[0],word_items2[1])
			morphs.append(morph)
		else:
			chunk = Chunk(morphs,dst,srcs)
			sent.append(chunk)	
			text.append(sent)
			morphs = []
			sent = []
			srcs_dict = defaultdict(lambda :[])
	return text

if __name__ == "__main__":
	text_chunk = cabtxt2chunk_inputter(sys.stdin)
	txtlist_opener(text_chunk,object_printer)
