# https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/2378/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse_extra(head):
            if head.next == None:
                return head, head
            last, first = reverse_extra(head.next)
            head.next = None
            last.next = head
            return head, first
        if head == None:
            return head
        return reverse_extra(head)[1]
