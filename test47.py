#!/user/bin/python
#-*-coding:utf-8-*-
#(47) (42)から(46)までの処理を１つのプログラムに統合し，処理内容をコマンドライン引数でOn/Offできるようにせよ．
#コマンドライン引数の処理には，optparseモジュールを用い，
#オプションには適当な名前（例えば(42)は--verbなど）とドキュメント（-hを引数にすることで表示される）を書け．


import optparse,pickle
from test42 import verb_extractor
from test43 import verb_base_extractor
from test44 import noun_sahenn_extractor
from test45 import AnoB_extractor
from test46 import noun_connection_extractor

text = pickle.load(open("test41_output.pickle","r"))

#parser
parser = optparse.OptionParser()
parser.add_option('-t','--text') #テキストファイルのアドレス
parser.add_option('-v','--verb',action='store_true')
parser.add_option('-b','--verb_base',action='store_true')
parser.add_option('-s','--noun_sahenn',action='store_true')
parser.add_option('-n','--AnoB',action='store_true')
parser.add_option('-c','--noun_connection',action='store_true')
options, args = parser.parse_args()

#test42:動詞を抜き出す
if options.verb:
	verb_extractor(text)

#test43:動詞の基本形を出力 
if options.verb_base:
	verb_base_extractor(text)

#test44:サ変名詞を出力
if options.noun_sahenn:
	noun_sahenn_extractor(text)

#test45:AのBという表現を抜き出せ
if options.AnoB:
	AnoB_extractor(text)

#test46:文章中のすべての名詞の連接（１形態素以上）を抜き出せ．
if options.noun_connection:
	noun_connection_extractor(text)

