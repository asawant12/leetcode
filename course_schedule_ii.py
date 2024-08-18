#https://leetcode.com/problems/course-schedule-ii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mapping = {}
        schedule = []
        visited = set()
        cycle = set()

        def find_dep(pre_req):
            if pre_req in cycle:
                return False
            if pre_req in visited:
                return True
            cycle.add(pre_req)
            for pr_rq in mapping[pre_req]:
                if find_dep(pr_rq) == False:
                    return False
            cycle.remove(pre_req)
            visited.add(pre_req)
            schedule.append(pre_req)

        mapping = { course : [] for course in range(numCourses)}
        for course,pre_req in prerequisites:
            mapping[course].append(pre_req)
    
        for course in mapping:
            if find_dep(course) == False:
                return []
        return schedule






        

