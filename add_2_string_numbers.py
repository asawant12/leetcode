# https://leetcode.com/problems/add-strings/
class Solution:
    
    def pad_zeros(self, num1_lst, num2_lst):
        if len(num1_lst) > len(num2_lst):
            shorter = num2_lst
            longer = num1_lst
        else:
            shorter = num1_lst
            longer = num2_lst
        req_length = len(longer) - len(shorter)
        for index in range(req_length):
            shorter.insert(0, 0)
        return shorter, longer
            
        
    def addStrings(self, num1: str, num2: str) -> str:
        num1_lst = list(num1)
        num2_lst = list(num2)
        shorter, longer = self.pad_zeros(num1_lst, num2_lst)
        shorter.reverse()
        longer.reverse()
        carry = 0
        addition = []
        for index in range(len(longer)):
            total = int(longer[index]) + int(shorter[index]) + carry
            if total > 9:
                carry =  1
                total = total - 10
            else:
                carry = 0
            addition.append(str(total))
        if carry == 1:
            addition.append(str(carry))
        addition.reverse()
        return "".join(addition)
        
        
