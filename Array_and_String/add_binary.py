# https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        if len_a >= len_b:
            max_str = a
            min_str = b
            min_len = len_b
            max_len = len_a
        else:
            max_str = b
            min_str = a
            min_len = len_a
            max_len = len_b
        result = []
        carry = 0
        for index in range(min_len):
            char_a = int(min_str[min_len - index-1])
            char_b = int(max_str[max_len - index -1])
            current_result = carry + char_a + char_b
            if current_result >=2:
                carry =1
            else:
                carry =0
            result.append(str(current_result%2))
        for index in range(min_len, len(max_str), 1):
            char_b = int(max_str[max_len - index -1])
            current_result = carry + char_b
            if current_result >=2:
                carry =1
            else:
                carry =0
            result.append(str(current_result%2))
        if carry == 1:
            result.append("1")
        return "".join(reversed(result))
