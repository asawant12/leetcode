#https://leetcode.com/problems/find-anagram-mappings/

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        indices = []
        for num in A:
            indices.append(B.index(num))
        return indices
