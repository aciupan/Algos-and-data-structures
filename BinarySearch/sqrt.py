# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 4:
            return 1
        if x == 4:
            return 2
        # binary search
        left = 2
        right = x //3 +1
        while right - left >1:
            middle = (right + left) // 2
            square_middle = middle * middle
            if square_middle == x:
                return middle
            if x > square_middle:
                left = middle
            else:
                right = middle
        # if nothing is returned at this point, sqrt(x) is between left and right
        return left
