# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ans = 0
        mapping = {}
        vovels_to_index = {'a': 0, 'e': 1, 'i': 2, 'o':3, 'u':4}
        vovels = [0]*5
        mapping[tuple(vovels)] = -1
        for indx, char in enumerate(s):
            if char in "aeiou":
                vovels[vovels_to_index[char]] = (vovels[vovels_to_index[char]]+1)%2
            mapping_key = tuple(vovels)
            if mapping_key in mapping:
                ans = max(ans, (indx - mapping[mapping_key]))
            else:
                mapping[mapping_key] = indx

        return ans
