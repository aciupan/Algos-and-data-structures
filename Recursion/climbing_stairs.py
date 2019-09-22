# https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1662/
class Solution(object):
    def climbStairs(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        if N == 1:
            return 1
        a_n_minus_2 = 1
        a_n_minus_1 = 1
        current_n = 1
        while current_n < N:
            a_n = a_n_minus_2 + a_n_minus_1
            a_n_minus_2 = a_n_minus_1
            a_n_minus_1 = a_n
            current_n +=1
        return a_n
        
