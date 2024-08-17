# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/description/

class Solution:
    def substr_is_unique(self, substr) -> bool:
        cnt_dt = {}
        for item in substr:
            if item in cnt_dt:
                return False
            else:
                cnt_dt[item]=1
        return True
    
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        s_list = list(s)
        start = 0
        end = k
        if len(s_list) < k:
            return 0
        uniq_cnt = 0
        while end <= len(s_list):
            substr = s_list[start:end]
            if self.substr_is_unique(substr):
                uniq_cnt +=1
            start += 1
            end +=1
        return uniq_cnt



