#!/usr/bin/python
#-*-coding:utf-8-*-
#cat test25_output.txt|python test30.py

import sys
from stemming.porter2 import stem

for line in sys.stdin:
    word = line[:-1].split('	')
    word_stem = stem(word[1])
    linedash = word[0]+"	"+word[1]+"	"+word_stem
    print linedash