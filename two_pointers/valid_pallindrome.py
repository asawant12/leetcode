# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left].isalnum() and s[right].isalnum() and (s[left] != " " or s[right] != " "):
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
            else:
                if not s[left].isalnum() or s[left] == " ":
                    left += 1
                if not s[right].isalnum() or s[right] == " ":
                    right -= 1
        return True
