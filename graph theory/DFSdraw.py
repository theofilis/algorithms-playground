#! /usr/bin/env python
# -*- coding: UTF8 -*-

import pygraphviz as pgv

def draw(A, imgdir, title):
	A.layout() # layout with default (neato)
	A.draw('{0}/{1}.svg'.format(imgdir,title)) # draw png
	print "Wrote %s.svg"%title

def initgraph(G,imgdir):
	A=pgv.AGraph(directed=True)
	A.graph_attr['splines']='true'
	A.graph_attr['overlap']='true'
	A.node_attr['style']='filled'
	A.node_attr['height']='0.1'
	A.node_attr['width']='0.1'
	A.edge_attr['arrowhead']='vee'
	A.edge_attr['len']='1.5'
	for u, ud in G.items():
		for v in ud[3]:
			A.add_edge(u,v)
		n = A.get_node(u) 
		n.attr['fillcolor']= ud[0]
	
	draw(A, imgdir, "Start")
	return A

def draw_step(A, imgdir, j, i, color):
	n = A.get_node(i)
	n.attr["fillcolor"] = color
	draw(A, imgdir, "Step%s"%j)
	return A

grey =  '#737373'
white = '#FFFFFF'
red = '#FF0000'
