# https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        left = 0
        right = len(nums) -1
        while right - left >1:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            if target > nums[middle]:
                left = middle
            else:
                right = middle
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1
