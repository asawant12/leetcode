# Python 3
import sys, json
import pprint
# Read from stdin         
locations = [
  {"id": 1, "name": "San Francisco Bay Area", "parent_id": None},
  {"id": 2, "name": "San Jose", "parent_id": 3},
  {"id": 3, "name": "South Bay", "parent_id": 1},
  {"id": 4, "name": "San Francisco", "parent_id": 1},
  {"id": 5, "name": "Manhattan", "parent_id": 6},
  {"id": 6, "name": "New York", "parent_id": None}
]
locations_hir = {}

def find_roots(locations):
    return [loc for loc in locations if not loc['parent_id']]

def find_nonroots(locations):
    return [loc for loc in locations if loc['parent_id']]

def find_leaf(root):
  for loc in find_nonroots(locations):
    if loc['parent_id'] == root['id']:
      if root['name'] not in locations_hir:
        locations_hir[root['name']] = []
      locations_hir[root['name']].append(loc['name'])
      find_leaf(loc)

def print_tree(root,level):
  for leaf in locations_hir[root]:
    print(level+ leaf)
    if leaf in locations_hir:
      print_tree(leaf,level+'-')
    
# Write to stdout
roots=find_roots(locations=locations)

for root in roots:
  locations_hir[root['name']]=[]
  find_leaf(root)
  locations_hir[root['name']] = sorted(locations_hir[root['name']])
  print(root['name'])
  print_tree(root['name'],'-')
  
  
  #output should be as under
  '''
  San Francisco Bay Area
-San Francisco
-South Bay
--San Jose
New York
-Manhattan
  
  '''
