# https://leetcode.com/explore/learn/card/binary-search/135/template-iii/944/
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums ==[]:
            return [-1, -1]
        if len(nums) ==1 :
            if nums[0] == target:
                return [0, 0]
            return [-1, -1]
        left = 0
        right = len(nums) -1
        if nums[0] > target or nums[-1] < target:
            return [-1, -1]
        while right - left > 1:
            middle = (right + left) // 2
            if target <= nums[middle]:
                right = middle
            else:
                left = middle +1
        if nums[left] == target:
            leftmost_index = left
        elif nums[right] == target:
            leftmost_index = right
        else:
            return [-1, -1]
        right = len(nums) -1
        while right - left > 1:
            middle = (right +left) //2
            if target>= nums[middle]:
                left=middle
            else:
                right = middle -1 
        if nums[right] == target:
            rightmost_index = right
        elif nums[left] == target:
            rightmost_index = left
        return [leftmost_index, rightmost_index]
            
        
