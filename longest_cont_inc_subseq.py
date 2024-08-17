# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        index = 0
        max_len = 0
        sub_seq = [nums[index]]
        while index < len(nums):
            if nums[index] > sub_seq[-1]:
                sub_seq.append(nums[index])
            else:
                max_len = max(len(sub_seq),max_len)
                sub_seq = [nums[index]]
            index += 1
        max_len = max(len(sub_seq),max_len)
        return max_len
        
