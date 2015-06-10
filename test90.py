#!/usr/bin/python
#-*-coding:utf-8-*-
#(90) 引数に渡された文字列を含むツイートを，RT数の多い順に表示するプログラムを実装せよ．

import pymongo
from pymongo import *
import re

if __name__ == '__main__':

	con = Connection('Tomo-no-MacBook-Pro.local')

	#コネクションからnlp100_tomoデータベースを取得
	db = con.nlp100_tomo

	#nlp100_tomoデータベースからtweetsコレクションを取得
	col = db.tweets

	query = raw_input("input_query : ")

	for data in col.find({"body":re.compile(query)}).sort("freq_rted",pymongo.DESCENDING):
		print "body : %s"%data["body"]
		print "freq_rted : %d"%data["freq_rted"]
		