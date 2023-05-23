# https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        stack = []
        for i in range(1,n+1):
            if target == stack:
                break
            stack.append(i)
            output.append("Push")
            if i not in target:
                stack.pop(-1)
                output.append("Pop")
        return output
            
