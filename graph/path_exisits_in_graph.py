# https://leetcode.com/problems/find-if-path-exists-in-graph/description/

# dfs
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        seen = set()

        if source == destination:
            return True

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        seen.add(source)

        def dfs(node):
            if node == destination:
                return True

            for ne in adj_list[node]:
                if ne not in seen:
                    seen.add(ne)
                    if dfs(ne):
                        return True

            return False
    
        return dfs(source)


# using stack

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        seen = set()
        stack = []
        if source == destination:
            return True

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        seen.add(source)
        stack.append(source)

        while stack:
            node = stack.pop()

            for ne in adj_list[node]:
                if ne == destination:
                    return True
                if ne not in seen:
                    seen.add(ne)
                    stack.append(ne)
        return False


# using Queue BFS

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        seen = set()
        q = deque([source])
        if source == destination:
            return True

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        seen.add(source)

        while q:
            node = q.popleft()

            for ne in adj_list[node]:
                if ne == destination:
                    return True
                if ne not in seen:
                    seen.add(ne)
                    q.append(ne)
        return False


