# https://leetcode.com/problems/valid-sudoku/description/
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set) # (r/3 , c/3)

        for r in range(9):
            for c in range(9):
                item = board[r][c]
                if  item == ".":
                    continue
                if (item in rows[r] or
                   item in cols[c] or
                   item in square[(r//3, c//3)]):
                   return False
                rows[r].add(item)
                cols[c].add(item)
                square[(r//3, c//3)].add(item)

        return True
