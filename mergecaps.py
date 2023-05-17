#! /usr/bin/python3

import difflib
import re
import sys

#x = difflib.SequenceMatcher(None, a, b).ratio()

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
	parts.append(txt)
	returnhash[keynum] = parts

	return returnhash

origcaptiondict = readsrt('scc_captions.srt')
premiereprodict = readsrt('prp_captions.srt')

#compare the two hashes

for key in origcaptiondict.keys():
	
	tc      = origcaptiondict[key][0]
	origtxt = origcaptiondict[key][1]

	txt = ''.join(sorted(origtxt.lower()))
	
	#print(txt)








