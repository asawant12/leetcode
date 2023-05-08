# https://leetcode.com/problems/check-if-matrix-is-x-matrix/
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        col = len(grid) - 1
        for row in range(len(grid)):
            if grid[row][row] == 0 or grid[row][col] == 0:
                return False
            else:
                grid[row][row] = grid[row][col] = -1
            col -= 1

        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] != -1 and grid[row][col] != 0:
                    return False
        return True
