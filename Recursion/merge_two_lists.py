# https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/2382/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l2 == None:
            return l1
        if l1 == None:
            return l2
        if l1.val <= l2.val:
            first = l1
            first.next = self.mergeTwoLists(l1.next, l2)
            return first
        else:
            first = l2
            first.next = self.mergeTwoLists(l1, l2.next)
            return first
