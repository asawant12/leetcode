# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def root_to_leaf(root, path_to_leaf):
            if root is None:
                return 0
            path_to_leaf = (path_to_leaf*10) + root.val
            if not root.left and not root.right:
                return path_to_leaf
            return root_to_leaf(root.left, path_to_leaf) + root_to_leaf(root.right, path_to_leaf)
        
        return root_to_leaf(root, 0)
