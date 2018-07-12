import hashlib as h
import bisect
from collections import defaultdict as d

A = [2, 7, 11, 15]
B = 9

N = 10000
# dictionary of tuples
H = d(list)
G = d(list)

# populate the hash tables
n = len(A)
for i in range(n):
    s = A[i]
    m = h.sha256(str(s).encode('utf-8'))
    hashvalue = int(m.hexdigest(),base=16) % N
    H[hashvalue].append(i)
    s = B - s
    m = h.sha256(str(s).encode('utf-8'))
    hashvalue = int(m.hexdigest(),base=16) % N
    G[hashvalue].append(i)
for j in range(n):
    s = A[j]
    m = h.sha256(str(s).encode('utf-8'))
    hashvalue = int(m.hexdigest(),base=16) % N
    for i in G[hashvalue]:
        if i < j:
            if A[i] + A[j] == B:
                return [i+1, j+1]
return []


# Check for collisions
#
#solution_list = []
#prev_sol = (n, n, n, n)
#for value in range(N):
#	found_equal_in_bin = 0
#    if value in H:
#        pairs_list = H[value]
#        l = len(pairs_list)
#        if l > 1:
#            for i in range(l):
#                for j in range(i+1, l):
#                    pair1 =  pairs_list[i]
#                    pair2 =  pairs_list[j]
#                    a = pair1[0]
#                    b = pair1[1]
#                    c = pair2[0]
#                    d = pair2[1]
#                    if a < c and b!=d and b != c and A[a]+A[b] == A[c]+A[d] and found_equal_in_bin == 0
#                        current_sol = (a, b, c, d)
#                        if current_sol < prev_sol:
#                            prev_sol = current_sol
#                        # basically, stop whenever we found the first pair of tuples with equal sum
#                        found_equal_in_bin = 1 
#if prev_sol != (n, n, n, n):
#    #prev_sol = list(prev_sol)
#    solution_list = list(prev_sol)
#return solution_list

