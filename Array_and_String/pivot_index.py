# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/
class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l <=2:
        	return -1
        s = 0
        for x in nums:
        	s+=x
        part_sum = 0
        for i in range(l):
        	if 2 * part_sum + nums[i] == s:
        		return i
        	part_sum += nums[i]
        return -1
