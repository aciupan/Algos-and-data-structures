# https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1139/
class MyHashSet(object):
    __slots__ = ["N", "main_array"]
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 1000
        self.main_array = [[] for x in range(1000)]
    def assign_bucket(self, key):
        return key % self.N
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket = self.assign_bucket(key)
        list_neighbors = self.main_array[bucket]
        for x in list_neighbors:
            if x == key:
                return
        self.main_array[bucket].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket = self.assign_bucket(key)
        list_neighbors = self.main_array[bucket]
        for index, x in enumerate(list_neighbors):
            if x == key:
                list_neighbors.pop(index)
                return
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucket = self.assign_bucket(key)
        list_neighbors = self.main_array[bucket]
        for x in list_neighbors:
            if x == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
