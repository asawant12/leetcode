# https://leetcode.com/problems/largest-number/submissions/1406103776/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = ""
        nums = [str(num) for num in nums]
        
        def compare(num1, num2):
            if (num1+num2) > (num2+num1):
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))
        ans = str(int("".join(nums)))
        return ans

        



                
