#!/usr/bin/python
#-*-coding:utf-8-*-
#(86) 83を実現するプログラムを実装せよ．なお，MongoDBをPythonから利用するときには，pymongoモジュールを用いる．
	#(83) MongoDBの対話型シェルを用い，特定のURLのツイートを検索せよ．

from pymongo import Connection
import json, sys



def main():
	con = Connection('YUKITOMO-MBA11.local')

	#コネクションからnlp100_tomoデータベースを取得
	db = con.nlp100_tomo

	#nlp100_tomoデータベースからtweetsコレクションを取得
	col = db.tweets

	#検索する特定のURL https://twitter.com/___licht/status/485830082703790081
	search_url = raw_input("input search_url\n") 

	for data in col.find({"url":search_url}):
		for k,v in data.items():
			print "%s : %s"%(k,v)


if __name__ == '__main__':
	main()
