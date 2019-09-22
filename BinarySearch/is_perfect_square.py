# https://leetcode.com/explore/learn/card/binary-search/137/conclusion/978/
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num in {0, 1, 4, 9}:
            return True
        if num <9:
            return False
        left = 0
        right = num//3
        while right - left > 1:
            middle = (right + left) //2
            mid_sq = middle * middle
            if mid_sq == num:
                return True
            if num > mid_sq:
                left = middle
            else:
                right = middle
        if left * left == num or right * right == num:
            return True
        return False
