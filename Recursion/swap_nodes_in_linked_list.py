# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        cursor = head.next
        if cursor == None:
            return head
        head.next = self.swapPairs(cursor.next)
        cursor.next = head
        return cursor
