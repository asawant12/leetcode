# https://leetcode.com/problems/kth-missing-positive-number/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr)-1
        while left <= right:
            mid = left+ (right-left)//2
            missing_till_mid = arr[mid] - (mid +1)
            if missing_till_mid < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k
