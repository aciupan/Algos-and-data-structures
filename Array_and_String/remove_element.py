# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1151/
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index_to_place_in = 0
        for cur_index in range(len(nums)):
            cur_value = nums[cur_index]
            if cur_value != val:
                nums[index_to_place_in] = cur_value
                index_to_place_in +=1
        return index_to_place_in
