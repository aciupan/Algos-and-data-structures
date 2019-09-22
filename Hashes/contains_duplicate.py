# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1112/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
