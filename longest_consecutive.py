# https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums:
            left_of_num = num - 1

            if left_of_num not in nums_set:
                seq_len = 0
                while (num + seq_len) in nums_set:
                    seq_len += 1
                if seq_len > max_len:
                    max_len = seq_len

        return max_len
