# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        output = -1
        haystack_len = len(haystack)
        needle_len = len(needle)
        if haystack_len == needle_len:
            if haystack == needle:
                output=0
            return output
        start_indx = 0
        end_indx = needle_len
        while end_indx <= haystack_len:
            if haystack[start_indx:end_indx] == needle:
                output = start_indx
                break
            start_indx += 1
            end_indx += 1
        return output
