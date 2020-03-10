# https://leetcode.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
        
    def reverseFirstK(self, k, head):
        """
        Reverses the first k nodes in a linked list
        Return the first and last nodes of the new list, 
        and the k+1 th node if present
        """
        
        # make sure length is >=k
        if head == None:
            return head, None, None
        cur_len = 1
        cur = head
        full_len = False
        while cur.next != None:
            cur = cur.next
            cur_len +=1
            if cur_len == k:
                full_len = True
                break
        if full_len == False:
            return head, None, None
        # we can reverse now
        last = head
        k_plus_1 = cur.next
        
        cur_len = 1
        previous = None
        current = head
        while cur_len <= k:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            cur_len +=1
        return previous, last, k_plus_1
            
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        _first, _last, _next = self.reverseFirstK(k, head)
        while _next != None:
            _nextfirst, _nextlast, _next = self.reverseFirstK(k, _next)
            _last.next = _nextfirst
            _last = _nextlast
        return _first
