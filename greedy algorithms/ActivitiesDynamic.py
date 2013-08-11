#! /usr/bin/env python
# -*- coding: UTF8 -*-

def activities(s, f):
	c = {}
	
	def init():
		for i in range(len(s), 0, -1):
			for j in range(i+1):
				c[i,j] = 0;
			
		return c;
	
	return init();

s = [1,3,0,5,3,5, 6, 8, 8, 2,12]
f = [4,5,6,7,8,9,10,11,12,13,14]
print(activities(s, f)[1,1])
