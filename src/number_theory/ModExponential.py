#! /usr/bin/env python
# -*- coding: UTF8 -*-

def even(n):
	if n%2 == 0:
		return True
	else:
		return False

def modexp(a, n, N):
	if n == 0:
		return 1;
	z = modexp(a, int(n/2), N)
	if even(n):
		return (z*z) % N
	else:
		return (a*z*z) % N


for i in range(10):
	print "modexp(%d, %d, 35) = %d" %(9, i, modexp(9, 2**i, 35))

for i in range(10):
	print "modexp(%d, %d, 35) = %d" %(4, i, modexp(4, 2**i, 35))

print "modexp(%d, %d, 35) = %d" %(4, 1536, modexp(4, 1536, 35))

