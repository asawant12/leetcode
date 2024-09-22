# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return []
        column_mapping = defaultdict(list)
        queue = deque([(root, 0, 0)])
        min_col = float("inf")
        max_col = float("-inf")

        while queue:
            node, row, col = queue.popleft()
            min_col = min(col, min_col)
            max_col = max(col, max_col)

            column_mapping[col].append((node.val, row))
            if node.left:
                queue.append((node.left, row+1, col-1))
            if node.right:
                queue.append((node.right, row+1, col+1))
        
        for col in range(min_col, max_col+1):
            items = column_mapping[col]
            items.sort(key = lambda x: (x[1] , x[0]))
            items = [val for val, _ in items]
            ans.append(items)
        return ans
      
