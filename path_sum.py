# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(currSum, root):
            if root is None:
                return False
            currSum += root.val
            if not root.left and not root.right:
                return currSum == targetSum
            return dfs(currSum, root.left) or dfs(currSum, root.right)
        return dfs(0, root)
