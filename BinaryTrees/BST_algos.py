# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Check if a given BST is valid

class Solution(object):
    def validate(self, root):
        # input: root
        # outputs: valid, min, max
        v_min = root.val
        v_max = root.val
        valid = 1
        q = root.left
        if q!= None:
            q_v, q_min, q_max = self.validate(q)
            if q_v == 0:
                valid = 0
            elif root.val > q_max:
                v_min = q_min
            else:
                valid = 0
        p = root.right
        if p != None:
            p_v, p_min, p_max = self.validate(p)
            if p_v == 0:
                valid = 0
            elif root.val < p_min:
                v_max = p_max
            else:
                valid = 0
        return valid, v_min, v_max
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        truthval = self.validate(root)[0]
        if truthval == 1:
            return True
        return False
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return []
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)

    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)
        parent = root
        while True:
            if val <= parent.val:
                if parent.left == None:
                    parent.left = TreeNode(val)
                    break
                parent = parent.left
            else:
                if parent.right == None:
                    parent.right = TreeNode(val)
                    break
                parent = parent.right
        return root
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        found = True
        parent = None
        node = root
        whichnode = 'none'
        while True:
            if node == None:
                return root
            if node.val == key:
                break
            if key < node.val:
                parent = node
                node = node.left
                whichnode = 'left'
            else:
                parent = node
                node = node.right
                whichnode = 'right'
        if node.left == None:
            if whichnode == 'none':
                return node.right
            if whichnode == 'left':
                parent.left = node.right
                return root
            else:
                parent.right = node.right
                return root
        if node.right == None:
            if whichnode == 'none':
                return node.left
            if whichnode == 'left':
                parent.left = node.left
                return root
            else:
                parent.right = node.left
                return root
        if node.right.left == None:
            node.right.left = node.left
            if whichnode == 'none':
                return node.right
            if whichnode == 'left':
                parent.left = node.right
                return root
            else:
                parent.right = node.right
                return root
        rm_par = node.right
        rm_node = rm_par.left
        while rm_node.left != None:
            rm_node = rm_node.left
            rm_par = rm_par.left
        rm_par.left = rm_node.right
        rm_node.right = node.right
        rm_node.left = node.left
        if whichnode == 'none':
            return rm_node
        if whichnode == 'left':
            parent.left = rm_node
            return root
        else:
            parent.right = rm_node
            return root
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == root:
            return root
        elif q == root:
            return root
        a = min(p.val, q.val)
        b = max(p.val, q.val)
        if a < root.val and b > root.val:
            return root
        elif a < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
    def height(self, root):
        if root == None:
            return 0, True
        a = self.height(root.left)
        b = self.height(root.right)
        if abs(a[0]-b[0]) <=1:
            truth = a[1] and b[1]
        else:
            truth = False
        return 1 + max(a[0], b[0]), truth
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.height[1]
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if l ==1:
            node = TreeNode(nums[0])
            return node
        if l == 0:
            return None
        mid = l //2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root






# Keep on returning the next smallest element
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.q = []
        if root != None:
            self.l_n_r(root.left)
            self.q.append(root.val)
            self.l_n_r(root.right)
    # traverse right - node - left
    def r_n_l(self, root):
        if root == None:
            return
        self.r_n_l(root.right)
        self.q.append(root.val)
        self.r_n_l(root.left)
    # traverse left - node - right
    def l_n_r(self, root):
        if root == None:
            return
        self.l_n_r(root.left)
        self.q.append(root.val)
        self.l_n_r(root.right)
    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.q) >0:
            return True
        return False
        

    def next(self):
        """
        :rtype: int
        """
        return self.q.pop(0)


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

