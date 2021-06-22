# https://leetcode.com/problems/basic-calculator-ii/
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = "".join(s.split())
        tokens = list(s)
        if not any(item in ["+","-","*","/"] for item in tokens):
            return s
        stack = []
        index = 0
        ans = 0
        operator = "+"
        current_number =""
        while index < len(tokens):
            if tokens[index] in ["+","-","*","/"] or (index == len(tokens)-1):
                if (index == len(tokens)-1):
                    current_number += tokens[index]
                if operator in ("*", "/"):
                    top_element = stack.pop()
                    if operator == "*":
                        top_element = top_element * int(current_number)
                    if operator == "/":
                        top_element = int(top_element / int(current_number))
                    stack.append(int(top_element))
                else:
                    current_number = operator+current_number
                    stack.append(int(current_number))
                current_number=""
                operator = tokens[index]
            else:
                current_number += tokens[index]
            index = index + 1

        for num in stack:
            ans = ans + num
        return ans
