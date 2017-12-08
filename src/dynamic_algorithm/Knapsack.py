#! /usr/bin/env python
# -*- coding: UTF8 -*-
import collections

Item = collections.namedtuple("Item", "c v")

def knapsack(items, S):
	DP = {0:0}
	
	def K(w):
		k = DP.get(w)
		if k == None:
			DP[w] = 0
		return DP[w]
	
	def fill():
		objects = []
		for w in range(1, S + 1):
			m = 0
			for item in items:
				wi, vi = item.c, item.v
				if wi <= w:
					temp = K(w - wi) + vi 
					if temp > m:
						m = temp
				else:
					break
			DP[w] = m 
		return DP
	
	return fill()

if __name__ == '__main__':
	S = 10
	items = [ Item(6,30), Item(3,14), Item(4,16), Item(2,9) ]
	print(knapsack(items, S)[10])
