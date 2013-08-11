#! /usr/bin/env python
# -*- coding: UTF8 -*-

# fibonacci series genarator function
#	Time complexity: EXPONENTIAL

time = { "i":0 , "j":0}

"""
	Time 	Complexity EXP
	Space Complexity O(1)
"""
def fib(n):
	time["i"] += 1
	if n <= 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

memo = {}
"""
	Time 	Complexity O(n)
	Space Complexity O(n)
"""
def mfib(n):
	time["j"] += 1
	try:
		try:
			return memo[n]
		except:
			if n <= 2:
				f = 1
			else:
				f = mfib(n-1) + mfib(n-2)
				memo[n] = f
			return f
	except:
		return "two many number"

num = {0:0, 1:1}
"""
	Time 	Complexity O(n)
	Space Complexity O(n)
"""
def nrfib(n):
	j = 0
	for i in range(2, n + 1):
		if (num.get(n-1) != None) and (num.get(n-2) != None):
			num[n] = num[n-1] + num[n-2]
			return num[n], j
		j += 1
		num[i] = (num[i-1] + num[i-2])
	return num[n], j

"""
	Time 	Complexity O(n)
	Space	Complexity O(1)
"""
def r1fib(n):
	a, b= 0, 1
	for i in range(1, n):
		a, b = b, a + b
	return b

def expirement(a):
	col = "# {0:^15} # {1:^15} # {2:^15} #"
	lin = "{0:#<55}".format('#')
	f, n = nrfib(a)
	print "# {0:^51} #".format("Result for fibonacci: " + str(a))
	print lin
	print col.format("fibonacci", "memorize", "nonrecursive")
	print lin	
	print col.format(fib(a), mfib(a), f)
	print col.format(time["i"], time["j"], n)
	print lin

a = 10
print r1fib(a)
#expirement(a)
#print num
#expirement(a+1)
