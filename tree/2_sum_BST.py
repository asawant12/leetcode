# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        node_values = set()

        def dfs(root):
            if not root:
                return False
            if k - root.val in node_values:
                return True
            else:
                node_values.add(root.val)
            return dfs(root.left) or dfs(root.right)

        return dfs(root)
