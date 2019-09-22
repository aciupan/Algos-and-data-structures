# https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        x = 0
        y = 0
        add = -1
        cur_s = 0
        max_x = len(matrix) -1
        if max_x == -1:
            return []
        max_y = len(matrix[0]) -1
        max_s = max_x + max_y +1
        res = []
        while cur_s < max_s:
            print(x, y)
            res.append(matrix[x][y])
            x += add
            y += -add
            if x < 0 or x > max_x or y < 0 or y > max_y:
                cur_s += 1
                if add == -1:
                    add = 1
                    if max_y >= cur_s:
                        x = 0
                        y = cur_s
                    else:
                        y = max_y
                        x = cur_s - max_y
                else:
                    add = -1
                    if max_x >= cur_s:
                        x = cur_s
                        y = 0
                    else:
                        x = max_x
                        y = cur_s - max_x
        return res
