# https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1134/
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dict_sum_nrpairs_1 = collections.defaultdict(int)
        dict_sum_nrpairs_2 = collections.defaultdict(int)
        for value_a in A:
            for value_b in B:
                dict_sum_nrpairs_1[value_a + value_b]+=1
        for value_c in C:
            for value_d in D:
                dict_sum_nrpairs_2[value_c + value_d]+=1
        nr_tuples = 0
        for sum_1, pairs_1 in dict_sum_nrpairs_1.items():
            if -sum_1 in dict_sum_nrpairs_2:
                nr_tuples += pairs_1 * dict_sum_nrpairs_2[-sum_1]
        return nr_tuples
