# https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        nr_strs = len(strs)
        if nr_strs == 1:
            return strs[0]
        lcp = []
        cur_index = 0
        arr_lenghts = [len(x) for x in strs]
        min_index_value = min(arr_lenghts)-1
        while cur_index <= min_index_value:
            # confirm that x[cur_index] is identical for all x in strs
            cur_char = strs[0][cur_index]
            cur_str_index = 1
            while cur_str_index < nr_strs:
                if strs[cur_str_index][cur_index] != cur_char:
                    return "".join(lcp)
                cur_str_index +=1
            # if we reach this step, x[cur_index] is identical for all x in strs
            lcp.append(cur_char)
            cur_index +=1
        return "".join(lcp)
