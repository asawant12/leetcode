# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        count = {}
        ans = 0

        for right in range(len(s)):
            sub_len = right - left + 1
            count[s[right]] = 1 + count.get(s[right], 0)

            while (sub_len - max(count.values())) > k:
                count[s[left]] -= 1
                left += 1
                sub_len = right - left + 1
            ans = max(ans, sub_len)
        return ans

