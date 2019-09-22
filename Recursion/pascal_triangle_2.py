# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/1660/
class Solution(object):
    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return [1]
        previous_rows = self.getRow(numRows-1)
        current_row = [1]
        for index in range(numRows-1):
            current_row.append(previous_rows[index] + previous_rows[index+1])
        current_row.append(1)
        return current_row
