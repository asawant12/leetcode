

closest = float('inf')
def find_closest(root, target):
  if root is None:
    return
  if abs(root.val - target) < abs(closest - target):
    closest = root.val
  if target < root.val:
    find_closest(root.left, target)
  elif target > root.val::
    find_closest(root.right, target)
  else:
    closest = root.val
    return


  find_closest(root, target)
