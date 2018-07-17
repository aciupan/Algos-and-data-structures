# Implementation of linked list operations.
# Source: https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
class Node:
    def __init__(self, value):
        self.val    = value
        self.next   = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        cur_node = self.head
        cur_index_traversed = 0
        while cur_node != None:
            if cur_index_traversed == index:
                return cur_node.val
            cur_node = cur_node.next
            cur_index_traversed += 1
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        temp = Node(val)
        temp.next = self.head
        self.head = temp

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        cur_node = self.head
        temp = Node(val)
        if cur_node == None:
            temp.next = cur_node
            self.head = temp
            return
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = temp

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        temp = Node(val)
        if index == 0:
            temp.next = self.head
            self.head = temp
        cur_index = 1 
        cur_node = self.head
        if cur_node == None:
            return
        while cur_node.next != None:
            if cur_index == index:
                temp.next = cur_node.next
                cur_node.next = temp
                break
            cur_node = cur_node.next
            cur_index += 1
        if cur_node.next == None and cur_index == index:
            temp.next = None
            cur_node.next = temp



    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """

        if self.head == None:
            return
        if index == 0:
            self.head = self.head.next
            return
        cur_node = self.head
        cur_index = 1
        while cur_node.next != None:
            if cur_index == index:
                cur_node.next = cur_node.next.next
                return
            cur_index +=1
            cur_node = cur_node.next

# Checks below:

        
def printlist(llist):
    cur_node = llist.head
    while cur_node != None:
        print(cur_node.val, "->", end= "")
        cur_node = cur_node.next
    print("end")

# Your MyLinkedList object will be instantiated and called as such:
#obj = MyLinkedList()
#q = obj.get(0)
#print(q)
#obj.addAtTail(2)
#printlist(obj)
#obj.addAtHead(5)
#obj.addAtHead(50)
#obj.addAtHead(500)
#obj.addAtTail(20)
#obj.addAtTail(30)
#printlist(obj)
#obj.addAtIndex(0, 10)
#printlist(obj)
#obj.deleteAtIndex(6)
#printlist(obj)

#print(q)
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)