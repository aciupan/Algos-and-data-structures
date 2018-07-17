# Input: array A and target B
# Output: indices (i+1, j+1) such that A[i] + A[j] = target
# Source: https://www.interviewbit.com/problems/2-sum/

import hashlib as h
import bisect
from collections import defaultdict as d

# Example inputs
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

