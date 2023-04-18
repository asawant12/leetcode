# https://leetcode.com/problems/longest-common-prefix/description/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        matching = True
        first = strs.pop(0)
        ptr=0
        while matching:
            if ptr < len(first):
                char = first[ptr]
            else:
                return prefix
            for string in strs:
                if ptr < len(string):
                    if char != string[ptr]:
                        return prefix
                else:
                    return prefix
            ptr += 1
            prefix += char
