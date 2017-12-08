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

x = [10,100,1000,10000]
d1 = timereport(exp, x, 2)
d2 = timereport(exp1, x, 2)
d3 = timereport(exp2, x, 2)


import numpy as np
import matplotlib.pyplot as plt

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)

y = [d[1] for d in d1]
ax0.plot(x, y)
ax0.set_title('exp')

y = [d[1] for d in d2]
ax1.plot(x, y)
ax1.set_title('exp1')

y = [d[1] for d in d3]
ax2.plot(x, y)
ax2.set_title('exp2')

# Tweak spacing between subplots to prevent labels from overlapping
plt.subplots_adjust(hspace=0.5)
plt.xlabel('n')
plt.show()