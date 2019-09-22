# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/
class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_nr = -1
        max_2nd = -1
        index = -1
        if len(nums) == 0:
            return -1
        for i, x in enumerate(nums):
            if x > max_nr:
                max_2nd = max_nr
                max_nr = x
                index = i
            elif x> max_2nd:
                max_2nd = x
        if max_nr >= 2*max_2nd:
            return index
        return -1
