#!/usr/bin/python
#-*-coding:utf-8-*-

def main(compere_text, item):
	one_sent_list = []
	com = []
	pere = []
	for line in open(compere_text):
		#print line
		compere_list = line.strip().split()
		com.append(compere_list[0])
		pere.append(compere_list[1])
	j=0
        for i in range(len(item) / 5):
                #print item[5*i]
                one_sent_list.append(item[5*i])
		#print item[5*i+3]
		if item[5*i+3] == 'B-NP':
			if com[j] != pere[j]:
				#print "aa"
				if com[j] != 'NONE' and pere[j] == 'NONE':
					one_sent_list.pop()
				elif com[j] == 'NONE' and pere[j] != 'NONE':
					one_sent_list.append(pere[j].lower())
				else:
					one_sent_list[-1] = pere[j].lower()
			j += 1
        print  one_sent_list

if __name__ == '__main__':
	import sys
	main(sys.argv[1], sys.argv[2:])

"""
#this
NONE w[0]=This hw=This hpos=DT hw|hpos=This|DT fw=This fpos=DT fw|fpos=This|DT w[-1]=None pos[-1]=None w[1]=is pos[1]=VBZ
# the pen
THE w[0]=pen hw=pen hpos=NN hw|hpos=pen|NN fw=pen fpos=NN fw|fpos=pen|NN w[-1]=is pos[-1]=VBZ w[1]=. pos[1]=i.
NONE NONE
THE A         
"""