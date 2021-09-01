# https://leetcode.com/problems/max-area-of-island/
class Solution:
    def search_neighbours(self, grid, row_index,island_index):
        grid[row_index][island_index]=0
        self.island_area += 1
            
        if island_index < (len(grid[row_index])-1):
            if grid[row_index][island_index+1] == 1:
                self.search_neighbours(grid, row_index, island_index+1)
        if row_index < (len(grid)-1):
            if grid[row_index+1][island_index] == 1:
                self.search_neighbours(grid, row_index+1, island_index)
        if island_index > 0:
            if grid[row_index][island_index-1] == 1:
                self.search_neighbours(grid, row_index, island_index-1)
        if row_index > 0:
            if grid[row_index-1][island_index] == 1:
                self.search_neighbours(grid, row_index-1, island_index)
                
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        self.island_area = 0
        for row_index in range(len(grid)):
            island_count = 0
            while True:
                try:
                    island_index = grid[row_index].index(1)
                except Exception:
                    break
                if grid[row_index][island_index] == 1:
                    self.search_neighbours(grid,row_index,island_index)
                    if self.island_area > self.max_area:
                        self.max_area = self.island_area
                    self.island_area = 0
        return self.max_area
