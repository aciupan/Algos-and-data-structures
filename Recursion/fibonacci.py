# https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1661/
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        a_n_minus_2 = 0
        a_n_minus_1 = 1
        current_n = 1
        while current_n < N:
            a_n = a_n_minus_2 + a_n_minus_1
            a_n_minus_2 = a_n_minus_1
            a_n_minus_1 = a_n
            current_n +=1
        return a_n
