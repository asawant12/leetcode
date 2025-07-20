# code to detect cycle in grap
from collections import defaultdict
edges = [[0, 1], [0, 2], [1, 2], [2, 0]]

adj_list = defaultdict(list)

for edge in edges:
    adj_list[edge[0]].append(edge[1])
    if edge[1] not in adj_list:
        adj_list[edge[1]] = []

UNVISITED, VISITING, VISITED = 0,1,2

states = [UNVISITED] * len(adj_list.keys())

def dfs(node):
    if states[node] == VISITING:
        return False
    elif states[node] == VISITED:
        return True
    else:
        states[node] = VISITING
        for dep in adj_list[node]:
            if not dfs(dep):
                return False
        states[node] = VISITED
        return True
            
if __name__ == '__main__':
    cycle = False
    for node in adj_list.keys():
        if not dfs(node):
            print("cycle detected")
            cycle = True
            break
    if not cycle:
        print(f"no cycle in graph:{adj_list}")
    
