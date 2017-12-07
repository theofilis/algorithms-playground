#! /usr/bin/env python
# -*- coding: UTF8 -*-

# x length n
# y length m
def grammar(x, y):
	n = len(x)
	m = len(y)
	cost = {'copy' 	 	: 1,
					'replace'	: 2,
					'delete'	: 3,
					'insert'	: 4,
					'twiddle'	: 5,
					'kill'		: 6}
	E = {(0,0):0}	
	
	def twiddle(i, j):
		if (n - i) < 2 or (m - j) < 2:
			return float('inf')
		else:
			if (x[i] == y[j+1]) and (x[i+1] == y[j]):
				return E[i-2, j-2] + cost['twiddle']
			else: return float('inf')
		
	def copy(i, j):
		if(x[i] == y[j]):
			return cost['copy']
		else:	
			return float('inf')
	
	def compute():
		for i in range(1, n):
			E[i,0] = cost['kill']
		for j in range(1, m):
			E[0,j] = cost['insert'] * j
		for i in range(1, n):
			for j in range(1, m):
				E[i,j] = min(E[i-1,j] + cost['delete'], 
										 E[i,j-1] + cost['insert'], 
										 E[i-1, j-1] + cost['replace'],
										 twiddle(i, j),
										 E[i-1, j-1] + copy(i, j))
		return E
	return compute()


if __name__ == '__main__':
	x = 'algorithm'
	y = 'altruistic'
	a = grammar(x, y)

	for i in range(len(x)):
			for j in range(len(y)):
				print(a[i,j],end="\t")
			print()

