#https://leetcode.com/problems/unique-paths/
class Solution:
    def n_choose_k(self, n, k):
        if k == 0:
            return 1
        return self.n_choose_k(n, k-1) * (n-k+1) // k
    def uniquePaths(self, m: int, n: int) -> int:
        if m <=n:
            return self.n_choose_k(m+n-2, m-1)
        return self.n_choose_k(m+n-2, n-1)
