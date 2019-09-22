# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1115/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_with_index = dict((value, index) for index, value in enumerate(nums))
        for index_a, value_a in enumerate(nums):
            if target - value_a in nums_with_index:
                if nums_with_index[target - value_a] != index_a:
                    return [index_a, nums_with_index[target - value_a]]
