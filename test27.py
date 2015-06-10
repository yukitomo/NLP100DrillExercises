#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from test10 import *

def main():
	f = open(sys.argv[1])
	word_counts = word_counter(f)
	top_n_order(word_counts,100)

if __name__ == '__main__':
	main()
