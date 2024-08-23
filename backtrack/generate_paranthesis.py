# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(openb, closeb, op):
            if openb == closeb == n:
                ans.append(op)
                return
            if openb < n:
                backtrack(openb+1, closeb, op+"(")
            if closeb < openb:
                backtrack(openb, closeb+1, op+")")
            return
        backtrack(0,0,"")    
        return ans
