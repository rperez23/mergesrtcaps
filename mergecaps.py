#! /usr/bin/python3

import re
import sys

origcaptiondict = {}
premiereprodict = {}

def readsrt(inf):

	parts = []
	txt   = '' 

	returnhash = {}

	try:
		srt = open(inf,'r')
	except:
		print('cannot open',inf)
		sys.exit(1)

	for l in srt.readlines():
		l = l.strip()
		#print(l)

		m1 = re.search('^(\d+)$',l)
		m2 = re.search('^\d{2}:\d{2}:\d{2},\d{3} -->',l)

		if m1:
			keynum = m1.group(1)
			#print(keynum)
		elif m2:
			tc  = l
			txt = ''
			parts.append(tc)
		elif l == '':
			parts.append(txt)
			returnhash[keynum] = parts
			parts = []
		else:
			txt += l

	srt.close()

	return returnhash

origcaptiondict = readsrt('scc_captions.srt')
premiereprodict = readsrt('prp_captions.srt')

print(origcaptiondict)






