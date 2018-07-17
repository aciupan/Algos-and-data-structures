# Breath first search in python

import numpy as np

# initialize the graph
graph = {5: [3, 1, 4], 
1:[2, 6],
2:[7, 0], 
6:[8, 0, 9]} 
root = 5
N = 10

# start the program
l = [root]
N = 10
visited = np.zeros(N)
while len(l) > 0 :
	num_in_level = len(l)
	for i in range(num_in_level):
		print(l[i], " ", end = "")
	print('\n')
	# Every time the while loop is initialized, the elements of l
	# are all the vertices from a given level. This level increases
	# by 1 every time
	for i in range(num_in_level):
		cur_vertex = l.pop(0)
		visited[cur_vertex] = 1
		# go through neighbors of the current vertex in the graph
		if cur_vertex in graph:
			num_neigh = len(graph[cur_vertex])
			for neigh_index in range(num_neigh):
				child = graph[cur_vertex][neigh_index]
				if visited[child] == 0 :
					visited[child] = 1
					l.append(child)	



