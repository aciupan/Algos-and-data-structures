# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1105/
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
        
