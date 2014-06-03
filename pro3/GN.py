#!/usr/bin/env python
import networkx
import networkx as nx

G = nx.Graph()
G.add_nodes_from(range(1,9))
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(2,3)
G.add_edge(3,5)
G.add_edge(5,4)
G.add_edge(4,6)
G.add_edge(5,8)
G.add_edge(5,6)
G.add_edge(6,7)

H = G.copy()
step = 0;

while True:
	step = step +1
	path_on_edge = []
	for i in G.nodes():
		for j in G.nodes():
			if i<j and nx.has_path(G,i,j):
				for p in nx.all_shortest_paths(G,i,j):
					for node in range(1, len(p)):
						path_on_edge.append((p[node-1],p[node]) if p[node-1]<p[node] else (p[node],p[node-1]))
	sheet = {}
	for edge in G.edges():
		sheet[edge] = path_on_edge.count(edge)
	
	print 'Step'+str(step)+':'
	print '-------------------------------------------------'
	for key, value in sorted(sheet.iteritems(), key=lambda (k,v): (v,k),reverse=True):
		if value == max(sheet.values()):
			char = '*'
			G.remove_edge(key[0],key[1])
		else:
			char = ' '
		print "%c %s: %s" % (char, key, value)
	print '-------------------------------------------------'

	if len(G.edges()) == 0:
		break


					


