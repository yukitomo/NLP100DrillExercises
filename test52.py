#!/usr/bin/python
#-*-coding:utf-8-*-
#(52) 形態素を表すクラスMorphを実装せよ．
#このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
#さらに，(51)の解析結果を１文毎に読み込み，１文をMorphオブジェクトのリストとして表現し，適当に表示するプログラムを実装せよ

#cat test51_japanese.txt |python test52.py 

import sys

class Morph:
	def __init__(self,surface,base,pos,pos1): #morphe=Morphe(surface,base,pos,pos1)
		#print '[Morph.__init__]'
		self.surface=surface
		self.base=base
		self.pos=pos
		self.pos1=pos1
	
	def showinfo(self):
		print  "[surface,base,pos,pos1] = [%s, %s, %s, %s]"%(self.surface, self.base, self.pos, self.pos1)

def cabtxt2morph_inputter():
	text=[] #text=[sent0,sent1,sent2,......]
	sent=[] #sent=[morph0,morph1,morph2,....] 1文をいれる
	for line in sys.stdin: #標準入力からcabochaの出力を受け取る
		line = line.strip()
		if not line[:2] == "* " and not line == "EOS":
			word_items=line.split("\t") # word_items=["表層系","名詞,サ変接続,*,*,*,*,編集,ヘンシュウ,ヘンシュー"]
			word_items2=word_items[1].split(",")
			morph = Morph(word_items[0],word_items2[6],word_items2[0],word_items2[1])
			sent.append(morph)
		elif line == "EOS":	
			text.append(sent)
			sent=[]
		else:pass
	return text

def txtlist_printer(text): #morph,chunk共に表示
	for i in range(len(text)):
		for j in range(len(text[i])):
			text[i][j].showinfo()
			if j == len(text[i])-1: #一文終わったとき空文字出力
				print "EOS"

def txtlist_opener(text,func):
	for i in range(len(text)):
		for j in range(len(text[i])):
			print "index : "+str(j)
			func(text[i][j])
			if j == len(text[i]) - 1: #一文終わったときにEOSを出力
				print "EOS"

def object_printer(obj):
	obj.showinfo()


if __name__ == "__main__":
	text = cabtxt2morph_inputter()
	txtlist_opener(text,object_printer)



