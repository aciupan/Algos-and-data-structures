# https://leetcode.com/explore/learn/card/binary-search/125/template-i/952/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # first, find the min in this array
        left = 0
        right = len(nums) -1
        if nums == []:
            return -1
        if nums[left] < nums[right]:
            # the array is ordered
            min_index = 0
        else:
            while right - left > 1:
                middle = (right + left) // 2
                if nums[left] > nums[middle]:
                    right = middle
                if nums[middle] > nums[right]:
                    left = middle
            # now, right - left = 1 and left > right
            min_index = right
        # now we found the index of the min number in the list
        if target == nums[min_index]:
            return min_index
        if target < nums[min_index]:
            return -1
        if min_index == 0 or min_index == len(nums) -1:
            left = 0
            right = len(nums) -1
        else:
            if target > nums[-1]:
                left = 0
                right = min_index -1
            else:
                left = min_index +1
                right = len(nums) -1
        # now we search between left and right
        if left > right:
            return -1
        while right - left > 1:
            middle = (right + left) // 2
            if target == nums[middle]:
                return middle
            if target < nums[middle]:
                right = middle -1
            elif target > nums[middle]:
                left = middle +1
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1
