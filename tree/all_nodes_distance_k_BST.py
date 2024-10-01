# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        parent = {}
        visited = set()

        def preorder(node):
            if node is None:
                return
            if node.left:
                parent[node.left] = node
            preorder(node.left)

            if node.right:
                parent[node.right] = node
            preorder(node.right)

        preorder(root)
        q = collections.deque()
        q.append(target)
        while q:
            if not k:
                break
            for _ in range(len(q)):
                node = q.popleft()
                visited.add(node.val)
                if node.left and node.left.val not in visited:
                    q.append(node.left)
                if node.right and node.right.val not in visited:
                    q.append(node.right)
                if node in parent and parent[node].val not in visited:
                    q.append(parent[node])
            k -= 1
        while q:
            res.append(q.popleft().val)

        return res
