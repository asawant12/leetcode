# https://leetcode.com/problems/find-all-anagrams-in-a-string/

import re
class Solution(object):
    combo = []
    def permute(self, data, i, length): 
        if i==length: 
            self.combo.append(''.join(data))
        else: 
            for j in range(i,length): 
             #swap
                data[i], data[j] = data[j], data[i] 
                self.permute(data, i+1, length) 
                data[i], data[j] = data[j], data[i] 
        
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        output = []
        p_list = list(p)
        self.permute(p_list,0, len(p_list))
        for test_sub in self.combo:
            op = [i.start() for i in re.finditer(test_sub, s)]
            output.extend(op)
        return output
                
