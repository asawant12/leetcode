# https://leetcode.com/problems/lemonade-change/
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change = {
            5 : 0,
            10: 0,
            20: 0
        }
        
        if bills[0] != 5:
            return False
        for bill in bills:
            chng = bill - 5
            if chng == 15:
                if change[10]:
                    change[10] -= 1
                    if change[5]:
                        change[5] -= 1
                    else:
                        return False
                else:
                    if change[5] >= 3:
                        change[5] -= 3
                    else:
                        return False
                    change[20] += 1
            if chng == 5:
                if change[5]:
                    change[5] -= 1
                    change[10] += 1
                else:
                    return False
            if chng == 0:
                change[5] += 1
        return True
