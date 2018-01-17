def level_order_print(root):
  if not root:
    return
   
   q = Queue()
   q.put(root)
   
   while not q.emptry():
    level_nodes = q.size()
    while level_nodes:
      node = q.get()
      print(node.data)
      if node.left:
        q.put(node.left)
      if node.rt:
        q.put(node.rt)
      level_nodes -= 1
    print("\n")
