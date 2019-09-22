# https://leetcode.com/explore/learn/card/n-ary-tree/131/recursion/919/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        if root.children == []:
            return 1
        return 1 + max([self.maxDepth(x) for x in root.children])
