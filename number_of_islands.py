'''
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''


class Solution:
    
    def check_island(self, row_index, col_index, rows, columns, grid):
        if row_index < 0 or col_index < 0 or row_index >= rows or col_index >= columns:
            return
        if grid[row_index][col_index] == "0":
            return
        else:
            grid[row_index][col_index] = "0"
            self.check_island(row_index+1, col_index, rows, columns, grid)
            self.check_island(row_index-1, col_index, rows, columns, grid)
            self.check_island(row_index, col_index+1, rows, columns, grid)
            self.check_island(row_index, col_index-1, rows, columns, grid)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return
        rows = len(grid)
        columns = len(grid[0])
        ans = 0
        for row_index in range(rows):
            for col_index in range(columns):
                if grid[row_index][col_index] == "1":
                    ans += 1
                self.check_island(row_index, col_index, rows, columns, grid)
        return ans
