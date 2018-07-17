# Detect if there is a cycle in a linked list
# Source: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current_slow = head
        if current_slow == None:
        	return False
        current_fast = head.next
        while current_fast != None:
        	current_fast = current_fast.next
        	if current_fast == None:
        		return False
        	current_fast = current_fast.next
        	if current_fast == None:
        		return False
        	current_slow = current_slow.next
        	if current_slow.val == current_fast.val:
        		return True
        return False


# Find the first node in the cycle of a linked list, if such a node exists
# Source: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
        	return 
        # cur_slow : goes through list one node at a time
        # cur_fast : goes through list two nodes at a time
        cur_slow = head
        cur_fast = cur_slow.next
        while cur_slow != cur_fast:
        	if cur_fast == None:
        		return 
        	cur_fast = cur_fast.next
        	if cur_fast == None:
        		return 
        	cur_fast = cur_fast.next
        	cur_slow = cur_slow.next
        # here, cur_slow = cur_fast and there is a cycle
        new_slow = head
        cur_slow = cur_slow.next
        while new_slow != cur_slow:
        	new_slow = new_slow.next
        	cur_slow = cur_slow.next
        # they will be equal at the first node in the cycle - the math just checks out
        return cur_slow

# Find the first note at the intersection of two linked lists, if such a node exists
# Source: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # There are three tracks : 0 - slow 1 - fast 2 - new_slow
        # code will show what they do. Each track has a turning node
        # where we jump to linked list B

        global turn_node_0
        global turn_node_1
        global turn_node_2
        turn_node_0 = None
        turn_node_1 = None
        turn_node_2 = None
        def next_node(node,trackid):
        	global turn_node_0
        	global turn_node_1
        	global turn_node_2
        	if trackid == 0:
        		if node.next == None:
        			if turn_node_0 == None:
        				turn_node_0 = node
        				node = headB
        			elif node == turn_node_0:
        				node = headB
        			else:
        				node = None
        		else:
        			node = node.next
        		return node
        	elif trackid == 1:
        		if node.next == None:
        			if turn_node_1 == None:
        				turn_node_1 = node
        				node = headB
        			elif node == turn_node_1:
        				node = headB
        			else:
        				node = None
        		else:
        			node = node.next
        		return node
        	elif trackid == 2:
        		if node.next == None:
        			if turn_node_2 == None:
        				turn_node_2 = node
        				node = headB
        			elif node == turn_node_2:
        				node = headB
        			else:
        				node = None
        		else:
        			node = node.next
        		return node
        if headA == None or headB == None:
        	return
        cur_slow = headA
        cur_fast = next_node(headA, 1)
        while cur_slow != cur_fast:
        	cur_fast = next_node(cur_fast, 1)
        	if cur_fast == None:
        		return
        	cur_fast = next_node(cur_fast, 1)
        	if cur_fast == None:
        		return
        	cur_slow = next_node(cur_slow, 0)
        # At this point, cur_slow == cur_fast and there is a common node
        new_slow = headA
        cur_slow = next_node(cur_slow, 0)
        while new_slow != cur_slow:
        	new_slow = new_slow.next
        	cur_slow = next_node(cur_slow, 0)
        # They equal at the first node that's common between the two lists
        return cur_slow

# Remove the n-th node from the end of a linked list. n will always be valid.
# Return the head of the list
# Source: https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def rm(cur, n):
        	if cur == None:
        		return 0, None
        	l, node = rm(cur.next, n)
        	l +=1
        	if l == n:
        		return l, cur
        	else:
        		return l, node

        # find the nth node
    	l, nth_node = rm(head, n)
    	if head == None:
    		return head
    	cur = head
    	if cur == nth_node:
    		head = nth_node.next
    		return head
    	if cur.next == None:
    		return
    	while cur.next != nth_node:
    		 cur = cur.next
    	# now we reach the node v such that v -> nth_node
    	cur.next = nth_node.next
    	return head


# Reverse a singly linked list
# Source: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head != None:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev

# Remove all elements from a linked list with a given value val
# Source: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return
        if head.val == val:
            return self.removeElements(head.next, val)
        head.next = self.removeElements(head.next, val)
        return head

# Reorder the nodes in a linked list, first odd-indexed nodes, then even-indexed nodes
# Source: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_iter  = head
        if head == None:
            return None
        even_iter = head.next
        if even_iter == None:
            return head
        node_iter = even_iter.next
        while node_iter != None:
            odd_iter.next = node_iter
            odd_iter = node_iter
            node_iter = node_iter.next
            if node_iter == None:
                break
            else:
                even_iter.next = node_iter
                even_iter = node_iter
                node_iter = node_iter.next
        odd_iter.next = head.next
        return head

# Find if a linked list is a palindrome
# Source: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        if head.next == None:
            return True
        l = 0
        cur = head
        while cur != None:
            l+=1
            cur = cur.next
        # l = length of the list
        mid = l//2
        add_1 = l % 2
        half_head = head
        l = 0
        # go to the ceiling(l/2) - th elem of the list
        while l < mid:
            half_head = half_head.next
            l +=1
        if add_1 == 1:
            half_head = half_head.next
        #reverse the first half of the list
        prev = None
        l = 1
        while l < mid:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
            l +=1
        head.next = prev
        # now compare the 1st half to the 2nd half
        l = 0
        while l <mid:
            #print(l)
            if head.val != half_head.val:
                return False
            head = head.next
            half_head = half_head.next
            l +=1
        return True

# In progress:

# Merge two sorted linked lists

class Solution(object):
    def progress(head, value):
        if head == None:
            return None
        cur = head
        while cur != None:

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """





    	

        		









