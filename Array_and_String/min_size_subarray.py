# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1299/
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums) == 1:
            if nums[0] >=s:
                return 1
            return 0
        cur_left = 0
        cur_right = 0
        cur_sum = nums[0]
        cur_min_interval_len = len(nums) +1
        while cur_right< len(nums)-1:
            if cur_sum >= s:
                # this is the first time it happens, and so [cur_left, cur_right]
                # is the smallest interval starting at cur_left with sum >= s
                cur_interval_len = cur_right - cur_left +1
                if cur_interval_len < cur_min_interval_len:
                    cur_min_interval_len = cur_interval_len
                cur_left +=1
                if cur_left > cur_right:
                    cur_right = cur_left
                    cur_sum = nums[cur_right]
                else:
                    cur_sum +=- nums[cur_left-1]
            else:
                # the sum is still smaller than s
                cur_right +=1
                cur_sum += nums[cur_right]
        if cur_right == len(nums) -1 :
            if cur_sum >=s:
                while cur_sum >=s and cur_left <= cur_right:
                    cur_interval_len = cur_right - cur_left +1
                    cur_sum += - nums[cur_left]
                    cur_left +=1
                if cur_interval_len < cur_min_interval_len:
                    cur_min_interval_len = cur_interval_len
        if cur_min_interval_len == len(nums) +1:
            return 0
        return cur_min_interval_len
