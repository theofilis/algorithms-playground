#! /usr/bin/env python
# -*- coding: UTF8 -*-
import sys

def palindrome(word):
	d = {}
	n = len(word)
	for i in range(n):
		d[i, i] = True

	for i in range(n-1):
		d[i, i+1] = word[i] == word[i+1]

	for s in range(2, n-1):
		for i in range(n-s):
			d[i, i+s] = word[i] == word[i+s] and d[i+1, i+s-1]

	return d

if __name__ == '__main__':
	d = palindrome("rapanaki")

	import pprint

	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(d)