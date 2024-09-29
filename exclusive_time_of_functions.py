# https://leetcode.com/problems/exclusive-time-of-functions/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        total_time_stamp = [0] * n
        stack = []
        prev_time_stamp = 0
        for log_snippet in logs:
            job_id,operation,time_stamp = log_snippet.split(":")
            job_id = int(job_id)
            time_stamp = int(time_stamp)
            if operation == "start":
                if len(stack) > 0:
                    total_time_stamp[stack[-1]] += time_stamp - prev_time_stamp
                stack.append(job_id)
                prev_time_stamp = time_stamp
            else:
                total_time_stamp[stack.pop()] += time_stamp - prev_time_stamp + 1
                prev_time_stamp = time_stamp + 1
        return total_time_stamp
