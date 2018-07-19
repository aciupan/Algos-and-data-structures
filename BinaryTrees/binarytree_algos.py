# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Preorder traversal
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        l = [root.val]
        return l + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

# Inorder traversal
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        return self.inorderTraversal(root.left) + [root.val]+ self.inorderTraversal(root.right)

# Postorder traversal
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        return self.postorderTraversal(root.left)+ self.postorderTraversal(root.right) + [root.val] 

# order traversal, i.e. BFS. 
# Source: https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
        	return []
        l = [[root.val]]
        q = [root]
        nodes_lvl = []
        last = root
        while len(q) != 0:
            v = q.pop(0)
            if v.left != None:
                nodes_lvl.append(v.left)
            if v.right != None:
                nodes_lvl.append(v.right)
        	# if last on level, update
            if v == last:
                if nodes_lvl == []:
                    break
                q = nodes_lvl
                values_lvl = [x.val for x in nodes_lvl]
                l.append(values_lvl)
                last = nodes_lvl[-1]
                nodes_lvl = []
        return l

# Max depth
# Source: https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/
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

# Is the tree symmetrical?
# Source: https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """        
        def smTrees(a, b):
            if a == None:
                if b == None:
                    return True
                return False
            if b == None:
                return False
            if a.val == b.val:
                return smTrees(a.left, b.right) and smTrees(a.right, b.left)
            return False
        if root == None:
            return True
        return smTrees(root.left, root.right)

# Is there a root-to-leaf path with a given sum?
# Source: https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/
    def hasPathSum(self, root, summ):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        a = root.left
        b = root.right
        v = root.val
        if a == None:
            if b == None:
                if v == summ:
                    return True
                return False
            return self.hasPathSum(b, summ - v)
        if self.hasPathSum(a, summ - v) == True:
            return True
        return self.hasPathSum(b, summ - v)

# Reconstruct tree from inorder and postorder
# Source: https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/942/
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder == []:
            return None
        val = postorder.pop(-1)
        #print(val)
        pos = 0
        while inorder[pos] != val:
            pos += 1
        node = TreeNode(val)
        lft_inorder = inorder[0:pos]
        rgh_inorder = inorder[(pos+1):]
        lft_postorder = postorder[0:pos]
        rgh_postorder = postorder[pos:]
        #print(lft_inorder, lft_postorder)
        #print(rgh_inorder, rgh_postorder)
        node.left = self.buildTree(lft_inorder, lft_postorder)
        node.right = self.buildTree(rgh_inorder, rgh_postorder)
        return node
















