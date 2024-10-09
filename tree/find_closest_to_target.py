

closest = float('inf')
def find_closest(root, target):
  if root is None:
    return
  if root.val == target:
    return root.val
  if abs(root.val - target) < abs(closest - target):
    closest = root.val
  if target < root.val:
    find_closest(root.left, target)
  else:
    find_closest(root.right, target)


  find_closest(root, target)
