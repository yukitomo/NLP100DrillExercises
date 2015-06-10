#!/usr/bin/python
#-*-coding:utf-8-*-
"""
inflection.table.txt には，英語の語彙（単語）に関する情報が収録されている。
このファイルは"|"区切り形式で，第１列に単語（活用あり），第２列に品詞，
第４列に活用形，第７列に基本形が格納されている．

(31) このファイルを読み込み，単語をキーとして，
品詞，活用形，基本形のタプルのリストを値とするマッピング型に格納せよ．
プログラムの動作を確認するため，標準入力から読み込んだ単語の語彙項目を閲覧する
プログラムを実装せよ．

(32) (31)で読み込んだマッピング型オブジェクトを，marshalモジュールを使ってファイルに書き出せ．
書き出したファイルを今後「辞書」と呼ぶ．
cat inflection.table.txt | python test31_32.py
"""
import sys,marshal

dictionary = {}
datafile=open('dictionary.dump', 'wb')
i = 0

for line in sys.stdin:
	i += 1
	print "number : " + str(i) #1690181
	boxes = line.split('|')
	#print boxes[0]
	#if boxes[0] in dictionary.keys(): めちゃくちゃ遅い
	try:
		dictionary[boxes[0]].append([boxes[1],boxes[3],boxes[6]])
		#print dictionary[boxes[0]]
	except:
		dictionary[boxes[0]] = [[boxes[1],boxes[3],boxes[6]]]
	
marshal.dump(dictionary,datafile)
