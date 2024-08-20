# https://leetcode.com/problems/group-anagrams/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_grps = defaultdict(list)
        for str_item in strs:
            mapping = [0] * 26
            for char in str_item:
                mapping_index = ord(char) - ord('a')
                mapping[mapping_index]+= 1
            key = tuple(mapping)
            anagram_grps[key].append(str_item)
        return list(anagram_grps.values())
