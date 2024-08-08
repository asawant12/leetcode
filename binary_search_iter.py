class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
    
        while right >= left:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
        return -1
        

        
