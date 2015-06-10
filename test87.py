#!/usr/bin/python
#-*-coding:utf-8-*-
#(87) 85を実現するプログラムを実装せよ．
	#(85) MongoDBの対話型シェルを用い，特定のユーザのツイートをRT数の多い順に10件まで検索せよ．

import pymongo
from pymongo import *

def main():

	con = Connection('YUKITOMO-MBA11.local')

	#コネクションからnlp100_tomoデータベースを取得
	db = con.nlp100_tomo

	#nlp100_tomoデータベースからtweetsコレクションを取得
	col = db.tweets


	search_user = raw_input("input search_user\n") 

	#top_count = col.find({"freq_rted":{"$gt":0}}).sort("freq_rted",pymongo.DESCENDING)
	top_count = col.find({"user":search_user}).sort("freq_rted",pymongo.DESCENDING).limit(10)
	
	for data in top_count:
		for k,v in data.items():
			print "%s : %s"%(k,v)

		print ""


if __name__ == '__main__':
	main()