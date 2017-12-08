#! /usr/bin/env python
# -*- coding: UTF8 -*-

def shortest_path(a, t, e, x, n):
	f = [[],[]]
	l = [[],[]]
	
	f[0] += [e[0] + a[0][0]]  
	f[1] += [e[1] + a[1][0]]
	
	for j in range(1, n):
		
		if f[0][j-1] + a[0][j] <= f[1][j-1] + t[1][j-1] + a[0][j]:
			f[0] += [f[0][j-1] + a[0][j]]
			l[0] += [1] 
		else:
			f[0] += [f[1][j-1] + t[1][j-1] + a[0][j]]
			l[0] += [2]
			
		if f[1][j-1] + a[1][j] <= f[0][j-1] + t[0][j-1] + a[1][j]:
			f[1] += [f[1][j-1] + a[1][j]]
			l[1] += [2]
		else:
			f[1] += [f[0][j-1] + t[0][j-1] + a[1][j]]
			l[1] += [1]

	m = n - 1
	if f[0][m] + x[0] <= f[1][m] + x[1]:
		fs = f[0][m] + x[0]
		ls = 1
	else:
		fs = f[1][m] + x[1]
		ls = 2		
	
	return f, l, fs, ls

def print_path(l, ls, n):
	i = ls
	print "γραμμή {0}, σταθμός {1}".format(i, n)
	for j in range(n, 1, -1):
		i = l[i-1][j-2]
		print "γραμμή {0}, σταθμός {1}".format(i, j-1)


####################################
a = [[7,9,3,4,8,4],
		 [8,5,6,4,5,7]]
t = [[2,3,1,3,4],
		 [2,1,2,2,1]]
e = [2, 4]
x = [3, 2]
n = len(a[0])
####################################
f, l, fs, ls = shortest_path(a, t, e, x, n)
####################################
print_path(l, ls, n)
