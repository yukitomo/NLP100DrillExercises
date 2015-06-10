#!/usr/bin/python
#-*-coding:utf-8-*-
"""
(80) 入力された英語の文に対して，各名詞句の冠詞のタイプを推定し，
誤りがあれば訂正を行うシステムを構築せよ
"""
import sys
import os, os.path
from test72 import *
from test62 import *
from geniatagger import *

def genia_tagger_input_sent(sent,tagger,output_file):
	"""
	入力されたセンテンスをGeniaTaggerにかける
	"""

	for item in tagger.parse(sent):
		output_file.write("\t".join(item)+"\n")

	output_file.write("EOS\n")


if __name__ == '__main__':
	tagger = GeniaTagger('/Users/yukitomo/Software/geniatagger-3.0.1/geniatagger')
	output_file = open("test80_output.genia", 'w')
	genia_tagger_input_sent(sys.argv[1], tagger, output_file)

	input_file = open("test80_output.genia", 'r')
	text = input_morph_txt(input_file)
	NPs = input_NP_text(text)

	write_file = open(input_file[:-9]+"f","w")

	for NP in NPs:
		write_file.write(NP.showinfo(),)