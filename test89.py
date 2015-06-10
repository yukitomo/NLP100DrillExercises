#!/usr/bin/python
#-*-coding:utf-8-*-
import pymongo
from pymongo import *

if __name__ == '__main__':
	con = Connection('YUKITOMO-MBA11.local')

	#コネクションからnlp100_tomoデータベースを取得
	db = con.nlp100_tomo

	#nlp100_tomoデータベースからtweetsコレクションを取得
	col = db.tweets

	for data in col.find({"bigram":"記憶"}):
		print data["body"]
		for item in data["bigram"]:
			print item
		