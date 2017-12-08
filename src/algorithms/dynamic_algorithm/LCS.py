#! /usr/bin/env python
# -*- coding: UTF8 -*-

def LCS(x, y):
	seen = { }
	def c(i, j):
		if i >= len(x) or j >= len(y) : return 0
		if (i, j) not in seen:
			if x[i] == y[j]:
				seen[i, j] = 1 + c(i + 1, j + 1)
			else:
				seen[i, j] = max(c(i + 1, j), c(i, j + 1))
		return seen[i, j]
	return c(0, 0)


x = 'HIEROGLYPHOLOGY vs. MICHAELANGELO'
y = 'HELLO'
print LCS(x, y)
