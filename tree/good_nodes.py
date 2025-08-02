# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float('-inf'))]
        good_nodes = 0
        while stack:
            node, max_till_now = stack.pop()
            if node.val >= max_till_now:
                good_nodes += 1
            if node.left:
                stack.append((node.left, max(node.val, max_till_now)))
            if node.right:
                stack.append((node.right, max(node.val, max_till_now)))
        return good_nodes
