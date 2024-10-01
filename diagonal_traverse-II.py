# https://leetcode.com/problems/diagonal-traverse-ii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag_mapping = collections.defaultdict(collections.deque)
        ROWS = len(nums)
        COLS = 0
        for row in range(ROWS):
            COLS = max(COLS, len(nums[row]))
        res = []
        for row in range(ROWS):
            for col in range(COLS):
                if col < len(nums[row]):
                    diag_mapping[row+col].appendleft(nums[row][col])
                else:
                    break

        for diag in diag_mapping:
            res.extend(diag_mapping[diag])
        return res
        
