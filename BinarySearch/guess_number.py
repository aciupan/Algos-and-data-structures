# https://leetcode.com/explore/learn/card/binary-search/125/template-i/951/
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==1:
            return 1
        left = 1
        right = n
        while right - left >1:
            middle = (left + right) // 2
            result = guess(middle)
            if result == 0:
                return middle
            if result == 1:
                left = middle + 1
            else:
                right = middle -1
        # if we reach this point, right - left = 1 or 0
        if guess(right) == 0:
            return right
        return left
