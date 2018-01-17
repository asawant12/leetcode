def is_BST(root):
  if not root:
    return True
  return helper(root,MIN,MAX)
  
def helper(root,MIN,MAX):
  if root.data < MIN or root.data > MAX:
    return False
  if root.left and ! helper(root.left,MIN,root.data)
    return False
  if root.rt and ! helper(root.rt,root.data,MAX)
    return False
