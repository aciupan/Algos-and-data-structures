# Implementation of linked list operations
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None


class MyLinkedList(object):

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
        if self.head == None:
            return -1
        cur = self.head
        i = 0
        while cur != None:
            if i == index:
                return cur.val
            i +=1
            cur = cur.next
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        if self.head == None:
            self.head = node
            return
        node.next = self.head
        self.head.prev = node.next
        self.head = node
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        if self.head == None:
            self.head = node
            return
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = node
        node.prev = cur

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        node = Node(val)
        if index == 0:
            if self.head == None:
                self.head = node
                return
            self.head.prev = node
            node.next = self.head
            self.head = node
            return
        if self.head == None:
            return
        cur = self.head
        if cur.next == None:
            if index == 1:
                cur.next = node
                node.prev = cur
            return
        i = 1
        while cur.next != None:
            if i == index:
                q = cur.next
                node.next = q
                node.prev = cur
                cur.next = node
                q.prev = node
                return
            i+=1
            cur = cur.next
        # if we reach this point, cur = last element of the list
        if i == index:
            cur.next = node
            node.prev = cur

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self.head == None:
            return
        if self.head.next == None:
            if index ==0:
                self.head = None
            return
        cur = self.head
        if index == 0:
            self.head = self.head.next
        i = 1
        while cur.next != None:
            #print(cur.val)
            if i == index:
                q = cur.next.next
                if q == None:
                    cur.next = None
                else:
                    q.prev = cur
                    cur.next = q
                return
            cur = cur.next
            i +=1
        
def printlist(llist):
    cur_node = llist.head
    while cur_node != None:
        print(cur_node.val, "<->", end= "")
        cur_node = cur_node.next
    print("end")

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(7)
obj.addAtHead(8)
obj.addAtTail(9)
obj.addAtTail(10)
obj.addAtIndex(2, 5)
printlist(obj)
obj.deleteAtIndex(1)
printlist(obj)
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)