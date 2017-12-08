#! /usr/bin/env python
# -*- coding: UTF8 -*-

def subsetset(S, n, B):
	M = {}

	def subset(S, n, B):
		M[0,0] = True
		for b in range(1, B+1):
			M[0, b] = False

		for i in range(1, n+1):
			for b in range(0, B+1):
				if S[i-1] > b:
					M[i, b] = M[i-1, b]
				else:
					M[i, b] = M[i-1, b] or M[i-1, b-S[i-1]]

	subset(S, n, B)

	i = n
	b = B
	A = set()

	while i != 0:
		if M[i, b] != M[i-1, b]:
			A.add(S[i-1])
			b = b - S[i-1]

		i = i - 1

	return M, A

if __name__ == '__main__':
	M, A = subsetset([4, 1, 2, 5], 4, 6)

	for a in A:
		print "item %d" % (a)