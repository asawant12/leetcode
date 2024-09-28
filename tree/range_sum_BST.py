# https://leetcode.com/problems/range-sum-of-bst/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        def preorder(root):
            if root is None:
                return 0
            if low<= root.val <= high:
                self.res += root.val
            if root.left:
                preorder(root.left)
            if root.right:
                preorder(root.right)
        preorder(root)
        return self.res
            




        
