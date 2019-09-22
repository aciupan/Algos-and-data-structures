# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/949/
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) -1
        while right - left > 1:
            if nums[left] < nums[right]:
                return nums[left]
            middle = (right + left) // 2
            if nums[left] > nums[middle]:
                right = middle
            else:
                left = middle +1
        if nums[left] < nums[right]:
            return nums[left]
        return nums[right]
