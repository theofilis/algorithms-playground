#! /usr/bin/env python
# -*- coding: UTF8 -*-

# x length n
# y length m
def grammar(x, y):
	n = len(x)
	m = len(y)
	cost = {'copy' 	 	: 2,
			'replace'	: 3,
			'delete'	: 4,
			'insert'	: 5,
			'twiddle'	: 1,
			'kill'		: 1}
	E = {(0,0):0}	
	O = {}
		
	def twiddle(i, j):
		try:	
			if (x[i] == y[j+1]) and (x[i+1] == y[j]):
				return E[i-2, j-2] + cost['twiddle']
			else: return float('inf')
		except:
			return float('inf')
		
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
				operate = {('delete',(i-1,j)):E[i-1,j] + cost['delete'], 
									 ('insert',(i,j-1)):E[i,j-1] + cost['insert'], 
									 ('replace',(i-1,j-1)):E[i-1, j-1] + cost['replace'],
									 ('twiddle',(i-2,j-2)):twiddle(i, j),
									 ('copy',(i-1, j-1)):E[i-1, j-1] + copy(i, j)
									 }
				min1 = float('inf')
				for op in operate.keys():
					temp = operate[op]
					if min1 > temp:
						min1 = temp
						O[i,j] = op 
				E[i,j] = min1
		return E,O
	return compute()

def printOperation(op, i , j):
	if i <= 0 or j <= 0:
		return ''
	a = op[i,j][0] + ' ' + printOperation(op, *op[i,j][1]) 
	return a

if __name__ == '__main__':
	x = ' algorithm'
	y = ' altruistic'
	a, b = grammar(x, y)
	print(printOperation(b, len(x)-1,len(y)-1))
	for i in  range(len(x)):
		for j in range(len(y)):
			print(a[i,j],end='\t')
		print()
	print()
	

def printA(x,y,a):
	for i in  range(0, len(x)):
		for j in range(0, len(y)):
			if i == j== 0:
				print('end',end='\t') 
			elif j == 0:
				print('kill',end='\t')
			elif i ==0:
				print(j,'*copy',sep='',end='\t')
			else:
				print(b[i,j][0],sep='',end='\t')
		print()
		
def printB(x,y,b):
	print()
	for i in  range(0, len(x)):
		for j in range(0, len(y)):
			if i == j== 0:
				print(i,'end',end='\t') 
			elif j == 0:
				print(i,'kill',end='\t')
			elif i ==0:
				print(j,'*copy',sep='',end='\t')
			else:
				print(b[i,j][1],sep='',end='\t')
		print()
	
