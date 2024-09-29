# https://leetcode.com/problems/is-subsequence/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)

        if s == "": return True
        if S > T: return False

        indx2 = 0
        for indx1 in range(T):
            if t[indx1] == s[indx2]:
                if indx2 == S - 1:
                    return True
                indx2 += 1
        return False
            
            
            

            
