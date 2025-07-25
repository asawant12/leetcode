# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for _ in range(numCourses):
            graph[_] = []
        for c1,c2 in prerequisites:
            graph[c1].append(c2)

        UNVISITED, VISITING, VISITED = 0,1,2
        state = [UNVISITED] * numCourses
        ans = []

        def dfs(crs):
            if state[crs] == VISITED:
                return
            elif state[crs] == VISITING:
                return True
            else:
                state[crs] = VISITING
                for pre in graph[crs]:
                    if state[pre] == VISITING:
                        return True
                    dfs(pre)
                state[crs] = VISITED
                if crs not in ans:
                    ans.append(crs)
        
        for cr in range(numCourses):
            if dfs(cr):
                return []
        return ans
            
