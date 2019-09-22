# https://leetcode.com/explore/learn/card/binary-search/137/conclusion/977/
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letters[-1] <= target:
            return letters[0]
        left = 0
        right = len(letters) -1 
        while right - left > 1:
            middle = (right + left) //2
            if letters[middle] > target:
                right = middle
            else:
                left = middle +1
        if letters[left] > target:
            return letters[left]
        return letters[right]
