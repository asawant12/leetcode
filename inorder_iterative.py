# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        traversal = []
        stack = []
        trav = root
        while trav is not None or len(stack) > 0:
            while trav is not None:
                stack.append(trav.left)
            trav = stack.pop()
            traversal.append(trav)
            trav = trav.right
        return traversal
