# https://leetcode.com/problems/even-odd-tree/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        q = collections.deque([root])
        level = 0
        index_level = ""

        def valid_node(value, index_level, first, level_nodes):
            if index_level == "EVEN":
                if value%2 == 0:
                    return False
                if not first and value <= level_nodes[-1]:
                    return False
                return True
            else:
                if value%2 != 0:
                    return False
                if not first and value >= level_nodes[-1]:
                    return False
                return True
        while q:
            level_nodes = []
            index_level = "ODD" if level%2 else "EVEN"
            for i in range(len(q)):
                first = True if i == 0 else False

                node = q.popleft()
                if not valid_node(node.val, index_level, first, level_nodes):
                    return False
                level_nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return True

        
        
