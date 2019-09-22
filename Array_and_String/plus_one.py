# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits) -1
        while l >=0:
            digits[l] +=1
            if digits[l] == 10:
                digits[l] = 0
                l +=-1
            else:
                break
        if l >= 0:
            return digits
        if digits[0] !=0 :
            return digits
        return [1] + digits
