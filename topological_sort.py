adj_list = { 1 : [0],
             2: [1],
             3: [2,0],
             5 : [6,4]}
             
visited = []
stack = []

def dfs(node):
    visited.append(node)
    if node in adj_list:
        for dep_node in adj_list[node]:
            if dep_node not in visited:
                dfs(dep_node)
    if node not in stack:
        stack.append(node)

for node in adj_list:
    if node not in visited:
        dfs(node)

for node in stack:
    print(node)
