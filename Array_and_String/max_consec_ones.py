# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1301/
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_streak_len = 0
        max_streak_len = 0
        for x in nums:
            if x == 1:
                current_streak_len +=1
            else:
                if current_streak_len > max_streak_len:
                    max_streak_len = current_streak_len
                current_streak_len = 0
        if current_streak_len > max_streak_len:
            max_streak_len = current_streak_len
        return max_streak_len
