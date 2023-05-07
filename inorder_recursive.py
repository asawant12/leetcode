# https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root is not None:
            if root.left is not None:
                op = self.inorderTraversal(root.left)
                output.extend(op)
            output.append(root.val)
            if root.right is not None:
                op = self.inorderTraversal(root.right)
                output.extend(op)
        return output
