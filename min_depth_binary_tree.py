# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        queue = [root]
        level = 0
        leaf_node = False
        
        while len(queue) >0:
            for index in range(len(queue)):
                trav = queue.pop(0)
                if trav.left:
                    queue.append(trav.left)
                if trav.right:
                    queue.append(trav.right)
                if trav.left == trav.right == None:
                    leaf_node = True
            level += 1
            if leaf_node:
                break
        return level
        
        
