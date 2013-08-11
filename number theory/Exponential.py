#! /usr/bin/env python
# -*- coding: UTF8 -*-

def even(n):
	if n%2 == 0:
		return True
	else:
		return False

def exp(a, n):
	if n == 0:
		return 1;
	z = exp(a, int(n/2))
	if even(n):
		return z*z
	else:
		return a*z*z

def exp1(a, n):
	p = 1
	for i in range(n):
		p *= a
	return p

def exp2(a, n):
	return a ** n	

from TimeMeasurements import timereport

print timereport(exp, [10,100,1000,10000], 2)

