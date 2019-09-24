# https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1029/
class Solution:
    def intersect_fromsorted(self, nums1, nums2):
        if nums1 == []:
            return []
        if nums2 == []:
            return []
        a_0 = nums1[0]
        b_0 = nums2[0]
        if a_0 == b_0:
            nums1.pop(0)
            nums2.pop(0)
            return [a_0] + self.intersect_fromsorted(nums1, nums2)
        if a_0 < b_0:
            nums1.pop(0)
            return self.intersect_fromsorted(nums1, nums2)
        nums2.pop(0)
        return self.intersect_fromsorted(nums1, nums2)
       
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.intersect_fromsorted(sorted(nums1), sorted(nums2))
