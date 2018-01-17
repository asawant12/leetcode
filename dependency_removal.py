'''
A : B
A : D
B : C
B : E
C : E
C : D
'''

Class Node:
  def __init(self,name):
    self.name = name
    self.edges= []
  
  def add_edge(self,node):
    self.edges.append(node)

resolved = []
seen = []

def resolve_dep(node,seen,resolved):
  seen.append(node)
  for edge in node.edges:
    if edge not in resolved:
      if edge in seen:
        raise "Cycle"
       resolve_dep(edge,seen,resolved)
    resolved.append(node)
  
