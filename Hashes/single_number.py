# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1176/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_singles = set()
        for x in nums:
            if x not in set_singles:
                set_singles.add(x)
            else:
                set_singles.remove(x)
        return set_singles.pop()
        
