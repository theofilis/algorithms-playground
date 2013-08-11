#! /usr/bin/env python
# -*- coding: UTF8 -*-
import numpy as np

def multiply(a, b):
	Ar, Ac = a.shape
	Br, Bc = b.shape
	if Ac != Br :
		return "Incompatible Dimensions."
	else:
		c = np.ones([Ar, Bc])
		for i in range(Ar):
			for j in range(Bc):
				c[i, j] = 0
				for k in range(Ac):
					c[i, j] = c[i, j] + a[i, k] * b[k, j]
		return c

def matrix_chain_order(p):
	report = "m[{0},{2}]+m[{3},{1}] + p[{0}]*p[{3}]*p[{8}] = {9}+{10} + {4}*{5}*{6} = {7}"
	n = len(p) - 1
	m = np.zeros([n,n])
	s = np.zeros([n,n])
	for l in range(2, n + 1):
		for i in range(n - l + 1):
			j = i + l - 1
			m[i, j] = float("inf")
			msg = " Take the minimum from: m[{0},{1}] ".format(i,j)
			print "{0:#^72}".format(msg)
			for k in range(i, j):				
				q = m[i, k] + m[k + 1, j] + p[i] * p[k+1] * p[j+1]
				if q < m[i, j]:
					m[i,j] = q
					s[i,j] = k
				print report.format(i,j,k,k+1,p[i], p[k+1], p[j+1], q,j+1, m[i,k], m[k+1, j])
			print "{0:#^72}".format("#")
			print m
			print "\n"
			#a = raw_input("next step: ")
	return m, s

def print_optimal_paren(s, i, j):
	if i == j:
		return "A{0}".format(int(i+1))
	else:
		a = print_optimal_paren(s, i, s[i,j])
		b = print_optimal_paren(s, s[i,j]+1, j)
		return "({0}{1})".format(a,b)

	
# Testing
a = np.array([[1, 2]])
b = np.array([[1, 2], [4, 5]])
m, s =matrix_chain_order([5, 10, 3, 12, 5, 50, 6])

print print_optimal_paren(s, 0,5)
