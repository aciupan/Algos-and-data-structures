# https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1171/
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
