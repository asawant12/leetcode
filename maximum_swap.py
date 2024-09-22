# https://leetcode.com/problems/maximum-swap/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = []
        digit_mapping = {}
        while num:
            dig = num%10
            digits.insert(0,dig)
            num = num//10
 
        for indx, n in enumerate(digits):
            digit_mapping[n] = indx

        found = False
        for indx, n in enumerate(digits):
            for i in range(9, -1, -1):
                if i > n and i in digit_mapping and digit_mapping[i] > indx:
                    temp = digits[indx]
                    digits[indx] = digits[digit_mapping[i]]
                    digits[digit_mapping[i]] = temp
                    found = True
                    break
            if found:
                break

        ans = 0
        for n in digits:
            ans = ans*10 + n
        return ans

        

