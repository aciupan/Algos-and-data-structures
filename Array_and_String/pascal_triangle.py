# https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        all_previous_rows = self.generate(numRows-1)
        previous_row = all_previous_rows[-1]
        current_row = [1]
        for index in range(numRows-2):
            current_row.append(previous_row[index] + previous_row[index+1])
        current_row.append(1)
        all_previous_rows.append(current_row)
        return all_previous_rows
