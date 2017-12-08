#! /usr/bin/env python3.2
# -*- coding: UTF8 -*-

import DFS
from DFSdraw import *

header = '''<!DOCTYPE html>
<html lang="en">
	<head>
		<title>{title}</title>
		<meta charset="utf-8" />
		<script type="text/javascript" src="slideshow.js"></script>
		<link href="slideshow.css" type="text/css" rel="stylesheet" media="all">
	</head>
	<body onLoad="animate();">
		<article>
		ΚΑΘΟΔΙΚΗ ΔΙΕΡΕΥΝΗΣΗ(G)
		</article><section>'''.format(title="Report dfs algorithm")

img = '''		<img id="{iid}" src="./img/{src}.png" />'''

footer = '''	</section></body>
</html>'''

def report(n, filename):
	fh = None
	try:
		fh = open(filename, "w")
		fh.write(header)
		fh.write(img.format(iid='current', src='Start'))
		for i in range(1, n+1):
			fh.write(img.format(iid='hide', src='Step[%d]'%i))
		fh.write(footer)
		return True
	except:
		return False

def main():
	n = DFS.dfs(DFS.G, 'Result/img')
	if report(n, 'Result/slideshow.html'):
		print "Report succesfully genarated"

if __name__ == '__main__':
	main()
