#! /usr/bin/env python
# -*- coding: UTF8 -*-
import sys

def minimun_cost_cut(D, n):
	cost = {}
	best = {}

	def P(i, j):
		return D[j] - D[i]

	for i in range(n):
		cost[i, i] = 0 

	for i in range(n-1):
		cost[i, i+1] = P(i, i+2)

	for d in range(2, n):
		for i in range(n-d):
			j = i + d

			cost[i, j] = sys.maxint
			best[i, j] = None

			for k in range(i, j):
				if (cost[i, j] > cost[i, k] + cost[k+1, j] + P(i, j+1)):
					cost[i, j] = cost[i, k] + cost[k+1, j] + P(i, j+1)
					best[i, j] = k

	return cost, best 

if __name__ == '__main__':
	A, best = minimun_cost_cut([0, 5, 8, 12, 14, 20, 24], 6)

	print best

	for j in range(6):
		for i in range(6-j):
			print A[i, i+j], "\t",
		print 