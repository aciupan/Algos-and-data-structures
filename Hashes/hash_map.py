# https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1140/
class MyHashMap(object):
    __slots__ = ["N", "main_array"]
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.N = 1000
        self.main_array = [[] for x in range(self.N)]
    def assign_bucket(self, key):
        return key%self.N
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        bucket = self.assign_bucket(key)
        for index, (cur_key, cur_value) in enumerate(self.main_array[bucket]):
            if cur_key == key:
                self.main_array[bucket][index] = (key, value)
                return
        self.main_array[bucket].append((key, value))

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket = self.assign_bucket(key)
        for index, (cur_key, cur_value) in enumerate(self.main_array[bucket]):
            if cur_key == key:
                return cur_value
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        bucket = self.assign_bucket(key)
        for index, (cur_key, cur_value) in enumerate(self.main_array[bucket]):
            if cur_key == key:
                self.main_array[bucket].pop(index)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
