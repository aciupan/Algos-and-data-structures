# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/1659/
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        cur_row = 1
        while cur_row < numRows:
            cur_row += 1
            cur_row_elem = [1]
            prev_row_elem = res[cur_row -2]
            for i in range(cur_row - 2):
                cur_row_elem.append(prev_row_elem[i] + prev_row_elem[i+1])
            cur_row_elem.append(1)
            res.append(cur_row_elem)
        return res
