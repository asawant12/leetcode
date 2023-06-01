# https://leetcode.com/problems/island-perimeter/

class Solution:
    def get_starting_index(self, grid):
        for index,row in enumerate(grid):
            try:
                col = row.index(1)
                return index, col
            except Exception as exp:
                print("Exception")
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = self.get_starting_index(grid)
        def dfs(grid, row, col, output=0, beg=True):
            if row > len(grid)-1 or col > len(grid[0])-1 or grid[row][col] == 0:
                return output
            else:
                addition_fact = 4 if beg is True else 3
                sub_fact = 0 if beg is True else 1
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    output = output + addition_fact - sub_fact
                    output = dfs(grid, row+1, col, output, False)
                    output = dfs(grid, row-1, col, output, False)
                    output = dfs(grid, row, col+1, output, False)
                    output = dfs(grid, row, col-1, output, False)
                    return output
        return dfs(grid, row, col)
            
            
