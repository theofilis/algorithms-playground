#! /usr/bin/env python
# -*- coding: UTF8 -*-

from DFSdraw import *

time = [0]

G = {
			'u':[white, 0, 0, 'vx'],
			'v':[white, 0, 0, 'y'],
			'w':[white, 0, 0, 'yz'],
			'x':[white, 0, 0, 'v'],
			'y':[white, 0, 0, 'x'],
			'z':[white, 0, 0, 'z']
		}

def visit(A, u, imgdir):
	G[u][0]  = grey
	time[0] += 1
	G[u][1] = time[0]
	draw_step(A , imgdir,time , u, G[u][0])
	for v in G[u][3]:
		if G[v][0] == white:
				visit(A, v, imgdir)

	G[u][0]  = red
	time[0] += 1
	G[u][2] = time[0]
	draw_step(A , imgdir, time, u, G[u][0])
	
def dfs(G, imgdir):
	A = initgraph(G, imgdir)
	for u in G.keys():
		if G[u][0] == white:
				visit(A, u, imgdir)
	return time[0]

initgraph(G, ".")
