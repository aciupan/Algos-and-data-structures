# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) -1
        while left < right:
            left_nr = numbers[left]
            right_nr = numbers[right]
            cur_sum = left_nr + right_nr
            if cur_sum == target:
                return [1+left, 1+right]
            if cur_sum > target:
                right +=-1
            else:
                left +=1
