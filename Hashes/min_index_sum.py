# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1177/
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict1_name_preference = dict((name, index) for index, name in enumerate(list1))
        dict2_name_preference = dict((name, index) for index, name in enumerate(list2))
        dict_sumranking_name = collections.defaultdict(list)
        for name, index in dict1_name_preference.items():
            if name in dict2_name_preference:
                index2 = dict2_name_preference[name]
                sum_rankings = index + index2
                dict_sumranking_name[sum_rankings].append(name)
        min_sumrank = len(list1) + len(list2)
        for sumrank in dict_sumranking_name.keys():
            if sumrank < min_sumrank:
                min_sumrank = sumrank
        return dict_sumranking_name[min_sumrank]
