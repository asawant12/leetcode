# https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, p: Optional[TreeNode], arr:[List]):
        if p.left is not None:
            arr.extend(self.inorderTraversal(p.left, arr))
        arr.append(p.val)
        if p.right is not None:
            arr.extend(self.inorderTraversal(p.right, arr))
        return arr
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q:
            return True
        if p is None or q is None:
            return False
        traversal_p = self.inorderTraversal(p, [])
        traversal_q = self.inorderTraversal(q, [])
        return (traversal_p == traversal_q)
