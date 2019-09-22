# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1117/
import collections
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        dict_f = dict()
        dict_inverse_f = dict()
        for index in range(len_s):
            char_s = s[index]
            char_t = t[index]
            if char_s not in dict_f:
                dict_f[char_s] = char_t
            else:
                if dict_f[char_s] != char_t:
                    return False
            if char_t not in dict_inverse_f:
                dict_inverse_f[char_t] = char_s
            else:
                if dict_inverse_f[char_t] != char_s:
                    return False
        return True
        
