# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/947/
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while right - left >1:
            middle = (right + left) // 2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle +1
        if isBadVersion(left):
            return left
        return right
