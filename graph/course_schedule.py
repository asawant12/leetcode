# https://leetcode.com/problems/course-schedule/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_mapping = defaultdict(list)
        for course, pre_req in prerequisites:
            course_mapping[course].append(pre_req)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        STATES = [0]*numCourses

        def dfs(crs):
            state = STATES[crs]
            if state == VISITED: return True
            elif state == VISITING: return False
            
            STATES[crs] = VISITING
            for pre in course_mapping[crs]:
                if not dfs(pre):
                    return False
            STATES[crs] = VISITED
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

