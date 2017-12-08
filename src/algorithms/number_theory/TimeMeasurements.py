#! /usr/bin/env python
# -*- coding: UTF8 -*-

import time

def measure(f, *karg):
	start_cpu = time.clock()
	start_real= time.time()
	n = f(*karg)
	end_cpu = time.clock()
	end_real = time.time()
	#print("%f Real Seconds" % (end_real - start_real))
	#print("%f CPU seconds" % (end_cpu - start_cpu))
	return n, (end_real - start_real), (end_cpu - start_cpu)

def timereport(f, n,*karg):
	stat = []
	for b in n:
		stat.append(measure(f,karg[0] ,b)[1:])
	return stat

