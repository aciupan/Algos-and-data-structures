# https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1168/
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m ==0:
            return []
        n = len(matrix[0])
        i_min = 0
        i_max = m-1
        j_min = 0
        j_max = n-1
        res = []
        while i_min <= i_max and j_min <= j_max:
            # W - E
            for j in range(j_min, j_max +1):
                res.append(matrix[i_min][j])
            # N - S
            if i_max != i_min:
                for i in range(i_min +1, i_max +1):
                    res.append(matrix[i][j_max])
            # E - W
                if j_min != j_max:
                    for j in range(j_max -1, j_min-1, -1):
                        res.append(matrix[i_max][j])
            # S - N
                    if i_max - i_min > 1:
                        for i in range(i_max -1, i_min, -1):
                            res.append(matrix[i][j_min])
            i_min +=1
            i_max +=-1
            j_min +=1
            j_max +=-1
        return res
