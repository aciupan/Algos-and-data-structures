# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        sum_max = 0
        for index in range(len(nums)//2):
            sum_max += nums[index *2]
        return sum_max
