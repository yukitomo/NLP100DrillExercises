#!/opt/local/bin/python
#-*-coding:utf-8-*-
#2015-02-10 Yuki Tomo

#cgi-bin/test99.py
#(100) 99で作ったプログラムを改変し，ブラウザ上からツイートを検索できるようにせよ

#chmod 755 test100.py



"""
mongod --dbpath ./set9_db データベースの起動
python -m CGIHTTPServer　ディレクトリcgi-binのある場所でローカルサーバーを起動

http://localhost:8000/cgi-bin/test99.py にアクセス

"""

import pymongo, re, cgi
from pymongo import *

con = Connection('Tomo-no-MacBook-Pro.local')

#コネクションからnlp100_tomoデータベースを取得
db = con.nlp100_tomo

#nlp100_tomoデータベースからtweetsコレクションを取得
col = db.tweets

print "Content-Type: text/html; charset=utf-8"
print

print '<html>'
print '<head><title>test100.py</title></head>'
print '<body>'

print '<h1>Input A Search Word</h1>'
print '<form action="test100.py" method="post"><input type="text" name="text" /><input type="submit" /></form>'

f = cgi.FieldStorage()
q = f.getfirst('text', '')

for data in col.find({"body":re.compile(q)}).sort("freq_rted",pymongo.DESCENDING):
	print '<p>'
	print "body : %s"%(data["body"].encode('utf-8'))
	print '</p>'
	print '<p>'
	print "freq_rted : %d"%data["freq_rted"]
	print '</p>'

print '</body></html>'
