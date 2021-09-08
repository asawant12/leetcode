# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

class Solution:
    def adjust(self, substring, char, k):
        substring += char
        for index in range(len(substring)):
            if len(set(substring[index:])) <= k:
                return substring[index:]
        return ""

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_len = 0
        substring = ""
        for char in s:
            if len(set(substring)) < k:
                substring += char
            else:
                max_len = max(max_len, len(substring))
                substring = self.adjust(substring, char, k)
                
        
        max_len = max(max_len, len(substring))
        return max_len
