# https://leetcode.com/problems/diet-plan-performance/description/

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        start = 0
        end = k
        days = len(calories)
        if end > days:
            return 0
        total_pts = 0
        cal_days = None
        while end <= days:
            if cal_days is None:
                cal_days = sum(calories[start:end])
            else:
                cal_days = cal_days - calories[start-1] + calories[end-1]
            if cal_days < lower:
                total_pts -= 1
            if cal_days > upper:
                total_pts += 1
            start += 1
            end += 1
        return total_pts
        
