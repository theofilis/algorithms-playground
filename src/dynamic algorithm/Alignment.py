#! /usr/bin/env python
# -*- coding: UTF8 -*-

def edit(x,y):
	E = {}
	m = len(x)
	n = len(y)
	
	def diff(i, j):
		if x[i] == y[j]:
			return 0
		else:
			return 1
	
	def distance():
		for i in range(m):
			E[i,0] = i
		for j in range(1,n):
			E[0,j] = j
		for i in range(1,m):
			for j in range(1,n):
				E[i, j] = min(E[i-1, j] + 1, E[i, j-1] + 1, E[i-1, j-1] + diff(i, j)) 
				
		return E
		
	return distance()

