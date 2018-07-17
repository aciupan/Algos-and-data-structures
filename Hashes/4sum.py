# Input: Array A
# Output: a list of all distinct indices i, j, k, l such that
# A[i] + A[j] + A[k] + A[l] = 0
# Source: https://www.interviewbit.com/problems/4-sum/
import hashlib as h
import bisect
from collections import defaultdict as d

A = [1, 0, -1, 0, 2, -2]
B = 0

# Number of buckets
N = 1000
# dictionary of tuples
H = d(list)
G = d(list)

# populate the hash tables
n = len(A)
for i in range(n):
	for j in range(i+1,n):
		pair = (i, j)
		s = A[i] + A[j]
		m = h.sha256(str(s).encode('utf-8'))
		hashvalue = int(m.hexdigest(),base=16) % N
		H[hashvalue].append(pair)
		minus_s = B - s 
		m = h.sha256(str(minus_s).encode('utf-8'))
		hashvalue = int(m.hexdigest(),base=16) % N
		G[hashvalue].append(pair)

# Check for collisions
solution_list = set()
for i in range(N):
	if i in H and i in G:
		h_list = H[i]
		g_list = G[i]
		for pair1 in h_list:
			for pair2 in g_list:
				index1 = pair1[0]
				index2 = pair1[1]
				index3 = pair2[0]
				index4 = pair2[1]
				if index2 < index3:
					a = A[index1]
					b = A[index2]
					c = A[index3]
					d = A[index4]
					if a + b + c + d == B:
						solution = tuple(sorted((a, b, c, d)))
						#print (type(solution))
						solution_list.add(solution)
						#bisect.insort(solution_list, solution)

return sorted(solution_list)
