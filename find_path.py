'''
{ 'A' : ['B','C'],
  'B' : ['C','D'],
  'C' : ['D'],
  'D' : ['C'],
  'E' : ['F'],
  'F' : ['C']
}
'''

def find_path(graph,start,end,path=[]):
    path.append(start)
    if start == end:
      return path
    if start not in graph:
      return None
    for node in graph[start]:
      if node not in path:
        new_path = find_path(graph,node,end,path)
        if new_path:
          return new_path
    return None
