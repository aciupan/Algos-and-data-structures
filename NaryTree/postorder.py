# https://leetcode.com/explore/learn/card/n-ary-tree/130/traversal/926/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        sol = []
        for child in root.children:
            sol += self.postorder(child)
        return sol + [root.val]
