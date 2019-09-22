# https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2380/
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n <0 :
            return self.myPow(1/x, -n)
        if n %2 == 0:
            a = self.myPow(x, n//2)
            return a*a
        else:
            a = self.myPow(x, (n-1)//2)
            return a*a*x
