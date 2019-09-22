# https://leetcode.com/explore/learn/card/n-ary-tree/130/traversal/915/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        current_vertices = [root]
        next_vertices = []
        all_vals = []
        while True:
            current_vals = []
            while current_vertices:
                cur_elem = current_vertices.pop(0)
                current_vals.append(cur_elem.val)
                next_vertices+= cur_elem.children
            all_vals.append(current_vals)
            if next_vertices ==[]:
                return all_vals
            current_vertices = next_vertices[::]
            next_vertices = []
