# https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1031/
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sub_findMin(left, right):
            if left == right:
                return nums[left]
            if right - left == 1:
                if nums[left] < nums[right]:
                    return nums[left]
                return nums[right]
            if nums[left] < nums[right]:
                return nums[left]
            middle = (right + left) //2
            if nums[left] > nums[middle]:
                return sub_findMin(left+1, middle)
            elif nums[middle] > nums[right]:
                return sub_findMin(middle+1, right)
            else:
                # nums[left] == nums[right] == nums[middle]
                return min(sub_findMin(left, middle), sub_findMin(middle+1, right))
        return sub_findMin(0, len(nums)-1)
