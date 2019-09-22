# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1131/
class Solution(object):
    def sp_function(self, n):
        if n < 10:
            return n*n
        return (n%10)**2 + self.sp_function(n//10)
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        set_prev_values = set()
        sp_val = self.sp_function(n)
        while sp_val not in set_prev_values:
            if sp_val == 1:
                return True
            set_prev_values.add(sp_val)
            sp_val = self.sp_function(sp_val)
        return False
