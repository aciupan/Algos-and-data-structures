# https://leetcode.com/explore/learn/card/binary-search/135/template-iii/945/
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        len_arr = len(arr)
        if arr == []:
            return []
        # if x smaller than all others, return first k elem
        if x <=arr[0]:
            return arr[0:k]
        # if x is the greatest, return last k elem
        if x >= arr[-1]:
            return arr[len_arr-k:]
        # otherwise, binary search etc
        # find first index where arr[i] >= x
        left = 0
        right = len_arr-1
        while right - left >1:
            middle = (right+left) //2
            if x > arr[middle]:
                left = middle +1
            else:
                right = middle
        # now, right - left = 1 or right = left
        right_index = None
        if arr[left] >= x:
            right_index = left
        else:
            right_index = right
        if right_index == 0:
            return arr[0:k]
        if x - arr[right_index-1] <= arr[right_index] - x:
            start_index = right_index -1
        else:
            start_index = right_index
        left_index = start_index
        right_index = start_index
        while right_index - left_index < k-1:
            if right_index == len_arr -1:
                left_index +=-1
            elif left_index == 0:
                right_index +=1
            else:
                if abs(arr[left_index-1] - x) <= abs(arr[right_index]-x):
                    left_index +=-1
                elif abs(arr[left_index-1] - x) <= abs(arr[right_index+1]-x):
                    left_index +=-1
                else:
                    right_index +=1
        return arr[left_index: right_index+1]
