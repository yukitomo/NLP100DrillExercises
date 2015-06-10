#!/opt/local/bin/python
#-*-coding:utf-8-*-
#2015-02-10 Yuki Tomo

#cgi-bin/test99.py
#(99) 90で作ったプログラムをCGIに改変し，「q」というパラメータで検索クエリを受け取り，検索結果をHTMLで出力せよ．

#chmod 755 test99.py



"""
mongod --dbpath ./set9_db データベースの起動
python -m CGIHTTPServer　ディレクトリcgi-binのある場所でローカルサーバーを起動

http://localhost:8000/cgi-bin/test99.py にアクセス

"""

import pymongo, re
from pymongo import *
from datetime import datetime

con = Connection('Tomo-no-MacBook-Pro.local')

#コネクションからnlp100_tomoデータベースを取得
db = con.nlp100_tomo

#nlp100_tomoデータベースからtweetsコレクションを取得
col = db.tweets

#検索クエリを取得
#q = raw_input("input_query : ")
q = "か"

print "Content-Type: text/html; charset=utf-8"
print

print '<html>'
print '<head><title>test99.py</title></head>'
print '<body>'

for data in col.find({"body":re.compile(q)}).sort("freq_rted",pymongo.DESCENDING):
	print '<h1>'
	print "body : %s"%(data["body"].encode('utf-8'))
	print '</h1>'
	print '<h1>'
	print "freq_rted : %d"%data["freq_rted"]
	print '</h1>'

print '</body></html>'
