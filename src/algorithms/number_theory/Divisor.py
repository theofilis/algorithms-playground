#! /usr/bin/env python
# -*- coding: UTF8 -*-

# Time complexity : O(1)
def divide(d, a):
	try:
		if d % a == 0:
			return True
		else:
			return False
	except ZeroDivisionError:
		return False

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def egcd(a, b):
	if b == 0:
		return a, 1, 0
	dt, xt, yt = egcd(b, a % b)
	d, x, y = dt, yt, xt - a/b*yt
	return d, x, y

a, b = 99, 78
d, x, y = egcd(a, b)
print a*x + b*y
