#! /usr/bin/env python
# -*- coding: UTF8 -*-

# d = {
#				('a',1):1
#			}
def compile(p,S):
	d = {}
	m = len(p) + 1
	for q in range(m):
		for a in S:
			k = min(m + 1, q + 2)
			k -= 1
			try:
				print p[0:q]+a
				print p[0:k]
			except:
				d[(q,a)] = 0

	return d

d = compile('aabab', 'ab')

for a in d.keys():
	print a, d[a]

