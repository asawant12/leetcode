# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = [root]
        level = 0

        while len(queue) >0:
            for index in range(len(queue)):
                trav = queue.pop(0)
                if trav.left:
                    queue.append(trav.left)
                if trav.right:
                    queue.append(trav.right)
            level += 1
        return level
