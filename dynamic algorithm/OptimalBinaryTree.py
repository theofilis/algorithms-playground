#! /usr/bin/env python
# -*- coding: UTF8 -*-

def optimal(p, q, n):
	e 	 = {}
	w 	 = {}
	root = {}
	for i in range(1, n + 1):
		e[i, i-1], w[i, i-1]= q[i-1], q[i-1]
	
	for l in range(1, n):
		for i in range(1, n-l+1):
			j = i + l -1
			e[i,j] = float('inf')
			w[i,j] = w[i,j-1] + p[j] + q[j]
			for r in range(i, j+1):
				t = e[i,r - 1] + e[r + 1, j] + w[i,j]
				if t < e[i,j]:
					e[i,j] = t
					root[i,j] = r
	
	return e, root
	
def printdiagonial(e, n,a=1):
	for i in range(a, n):
		for j in range(i, n):
			print( '%.2f'%e[i,j - 1], end=' ')
		print()

if __name__ == '__main__':
	p = [	 0, .15, .10, .05, .1, .2]
	q = [.05, .10, .05, .05, .05, .1]
	n = len(p)
	e, root =(optimal(p, q, n))	
	printdiagonial(e, n+1)
