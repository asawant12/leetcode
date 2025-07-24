# https://leetcode.com/problems/path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def dfs(node, curr_sum=0):
            if node is None:
                return False
            
            curr_sum += node.val
            if node.left is None and node.right is None:
                return curr_sum == targetSum
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
        return dfs(root)
                     
        
