# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1440/
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        len_s = len(s)
        for left_index in range(len_s//2):
            right_index = len_s-1 - left_index
            left_value = s[left_index]
            s[left_index] = s[right_index]
            s[right_index] = left_value
