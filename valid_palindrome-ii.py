#https://leetcode.com/problems/valid-palindrome-ii/
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        reverse_s = s[::-1]
        mis_match_counter = 0
        for index in range(len(s)):
            if s[index] != reverse_s[index]:
                del reverse_s[index]
                del s[index]
                break
        reverse_s = "".join(reverse_s)
        s = "".join(s)
        if (reverse_s == reverse_s[::-1]) or (s == s[::-1]):
            return True
        else:
            return False
