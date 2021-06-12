# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxp = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        self.postorder(root)
        return self.maxp
    
    def postorder(self, root: TreeNode):
        if root is None:
            return 0
        left = max(0, self.postorder(root.left))
        right = max(0, self.postorder(root.right))
        self.maxp = max(self.maxp, (left + right + root.val))
        return max(left, right) + root.val
        
