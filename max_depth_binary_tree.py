# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = []
        level = 0
        q = root
        queue.append(root)
        while q:
            trav = queue.pop(0)
            if trav.left:
                queue.append(trav.left)
            if trav.rt:
                queue.append(trav.right)
