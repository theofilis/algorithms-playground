#! /usr/bin/env python
# -*- coding: UTF8 -*-

def activities(s, f):
	n = len(s)
	A = [0]
	i = 0
	
	for m in range(1, n):
		if s[m] >= f[i] :
			A += [m]
			i = m
	
	return A;

s = [1,3,0,5,3,5, 6, 8, 8, 2,12]
f = [4,5,6,7,8,9,10,11,12,13,14]
print(activities(s, f)) # prints [0, 3, 7, 10]
