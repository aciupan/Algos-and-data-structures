# https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_needle = len(needle)
        len_haystack = len(haystack)
        current_index_in_haystack = 0 
        max_current_index_in_haystack = len_haystack - len_needle
        if needle == []:
            return 0
        if haystack == []:
            return -1
        while current_index_in_haystack <= max_current_index_in_haystack:
            if haystack[current_index_in_haystack:current_index_in_haystack + len_needle] == needle:
                return current_index_in_haystack
            current_index_in_haystack +=1
        return -1
