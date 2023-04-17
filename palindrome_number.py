#https://leetcode.com/problems/palindrome-number/description/
  
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_list = self.convert_to_list(x)
            orignal_x = x_list.copy()
            x_list.reverse()
            if orignal_x == x_list:
                return True
            else:
                return False 


    def convert_to_list(self, x:int) -> list:
        x_list = []
        while x>0:
            x_list.append(x%10)
            x = int(x/10)
        return x_list
