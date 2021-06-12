# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    lst_of_nodes = []
    
    def preorder_traversal(self, root):
        
        val = "N" if root is None else str(root.val)
        self.lst_of_nodes.append(str(val))
        if root is None:
            return
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)
        

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.lst_of_nodes = []
        if root is None:
            return ""
        self.preorder_traversal(root)
        return ",".join(self.lst_of_nodes)
    

    def dfs(self):
        if self.data[self.index] == "N":
            self.index += 1
            return None
        node = TreeNode(int(self.data[self.index]))
        self.index += 1
        node.left = self.dfs()
        node.right = self.dfs()
        return node
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
           return None
        self.data = data.split(",")
        self.index = 0
        root = self.dfs()
        return root
      
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
