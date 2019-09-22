# https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2375/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
        	return 0
        a = self.maxDepth(root.left)
        b = self.maxDepth(root.right)
        if a> b:
        	return 1 + a
        return 1+b
