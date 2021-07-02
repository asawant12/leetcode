# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# https://www.youtube.com/watch?v=xuvw11Ucqs8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def lowest_common_ancestor(self, root, p, q):
        if root is None:
            return False
        left = self.lowest_common_ancestor(root.left, p , q)
        right = self.lowest_common_ancestor(root.right, p , q)
        curr = (root.val == p.val) or (root.val == q.val)
        if (left and curr) or (right and curr) or (left and right):
            self.answer = root
        return left or right or curr

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.answer = TreeNode(0)
        self. lowest_common_ancestor(root, p, q)
        return self.answer
        
