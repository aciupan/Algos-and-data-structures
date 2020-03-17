# https://leetcode.com/problems/max-points-on-a-line/
import collections
import numpy as np
class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        if a == 0:
            return b
        return self.gcd(b, a%b)
    def reducefraction(self, a, b):
        gcd = self.gcd(a, b)
        return (a//gcd, b//gcd)
    def maxPoints(self, points: List[List[int]]) -> int:
        dict_line_count = collections.defaultdict(set)
        nr_points = len(points)
        if nr_points == 0:
            return 0
        if nr_points == 1:
            return 1
        for i in range(nr_points):
            for j in range(i+1, nr_points, 1):
                pt1 = points[i]
                pt2 = points[j]
                y_diff = pt1[1] - pt2[1]
                x_diff = pt1[0] - pt2[0]
                if x_diff == 0:
                    slope = "inf"
                    intercept = pt1[0]
                elif y_diff == 0:
                    slope = pt1[1]
                    intercept = "inf"
                else:
                    slope = self.reducefraction(y_diff, x_diff)
                    a_slope = slope[0]
                    b_slope = slope[1]
                    x1 = pt1[0]
                    y1 = pt1[1]
                    intercept = self.reducefraction(x1 * a_slope - y1 * b_slope, a_slope)
                dict_line_count[(slope, intercept)] |= {i, j}
        max_count = 1
        for value in dict_line_count.values():
            value = len(value)
            if value > max_count:
                max_count = value
        return max_count
