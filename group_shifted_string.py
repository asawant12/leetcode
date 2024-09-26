#https://leetcode.com/problems/group-shifted-strings/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        grouping_dict = defaultdict(list)
        for string in strings:
            if len(string) == 1:
                grouping_dict[(-1,)].append(string)
            else:
                chars_diff = []
                indx = 1
                while indx < len(string):
                    chars_diff.append((ord(string[indx])-ord(string[indx-1]))%26)
                    indx += 1
                grouping_dict[tuple(chars_diff)].append(string)
        return grouping_dict.values()
        
