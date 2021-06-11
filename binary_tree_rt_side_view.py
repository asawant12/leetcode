# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import Queue

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        view = []
        if not root:
            return view
        last_node=None
        q = Queue.Queue()
        q.put(root)
        while not q.empty():
            node_level = q.qsize()
            while node_level:
                node = q.get()
                if node:
                    last_node = node.val
                    if node.left:
                        q.put(node.left)
                    if node.right:
                        q.put(node.right)
                    node_level-=1
            view.append(last_node)
        return view
