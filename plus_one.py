# https://leetcode.com/problems/plus-one/submissions/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        index = len(digits)-1
        carry = 0
        digits[index] = digits[index] + 1
        while index >= 0:
            digits[index] = digits[index] + carry
            if digits[index] > 9:
                digits[index] = 0
                carry = 1
            else:
                carry = 0
            index -= 1
        if carry:
            digits.insert(0, carry)
        return digits
