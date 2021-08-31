# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")" : "(",
            "}" : "{",
            "]" : "["}
        stack = []
        
        for bracket in s:
            if bracket in mapping.keys():
                if len(stack) == 0:
                    return False
                else:
                    if mapping[bracket] == stack[-1]:
                        stack.pop()
                    else:
                        return False
            elif bracket in mapping.values():
                stack.append(bracket)
            else:
                return False
        
        if len(stack) != 0:
            return False
        else:
            return True
