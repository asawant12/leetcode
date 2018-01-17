def height(root):
  if not root:
    return 0
  lheight = height(root.lft)
  rheight = height(root.rt)
  if lheight > rheight:
    return (lheight + 1)
  else:
    return (rheight + 1)
