# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {}
        for char in s:
            hash_s[char] = 1 + hash_s.get(char, 0)
        for char in t:
            hash_t[char] = 1 + hash_t.get(char, 0)
        for char in hash_s:
            if char in hash_t:
                if hash_s[char] != hash_t[char]:
                    return False
            else: 
                return False
        return True
