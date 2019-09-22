# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/948/
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return -1
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums) -1
        while right - left > 1:
            middle = (right + left) / 2
            if nums[middle] > nums[middle-1] and nums[middle] > nums[middle+1]:
                return middle
            if nums[middle] > nums[middle-1] and nums[middle] < nums[middle+1]:
                left = middle +1
            else:
                right = middle -1
        if nums[right] > nums[left]:
            return right
        return left
