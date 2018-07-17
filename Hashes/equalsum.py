# Input: array A
# Output: the lexicographically smallest tuple (i, j, k, l) such that
# A[i] + A[j] = A[k] + A[l]
# Source: https://www.interviewbit.com/problems/equal/
import hashlib as h
import bisect
from collections import defaultdict as d

A = [ 0, 0, 1, 0, 2, 1 ]

N = 10000
# dictionary of tuples
H = d(list)

# populate the hash tables
n = len(A)
for i in range(n):
    for j in range(i+1,n):
        pair = (i, j)
        s = A[i] + A[j]
        m = h.sha256(str(s).encode('utf-8'))
        hashvalue = int(m.hexdigest(),base=16) % N
        H[hashvalue].append(pair)

for i in range(n):
    for j in range(i+1, n):
        s = A[i] + A[j]
        m = h.sha256(str(s).encode('utf-8'))
        hashvalue = int(m.hexdigest(),base=16) % N
        for pair in H[hashvalue]:
            k = pair[0]
            l = pair[1]
            if i < k and j != k and j != l:
                if s == A[k] + A[l]:
                    return [i, j, k, l]

# A second solution below:

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

