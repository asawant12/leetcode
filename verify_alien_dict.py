# https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution(object):
    def check_sorted(self, str1, str2, order_mapping):
        sorted_wrd = False
        length = len(str1) if len(str1) < len(str2) else len(str2)
        for str_idx in range(length):
            if order_mapping[str1[str_idx]] == order_mapping[str2[str_idx]]:
                continue
            elif order_mapping[str1[str_idx]] < order_mapping[str2[str_idx]]:
                sorted_wrd = True
                break
            else:
                return False
            
        if not sorted_wrd and len(str1) > len(str2):
            return False
        return True
            
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_mapping = dict(zip(order, range(len(order))))
        if len(words) == 1:
            return True
        if len(words) == 2:
            return self.check_sorted(words[0], words[1], order_mapping)
        for index in range(len(words)-2):
            sorted_chk = self.check_sorted(words[index], words[index+1], order_mapping)
            if not sorted_chk:
                return False
        return True
