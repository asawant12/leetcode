# https://leetcode.com/problems/spiral-matrix-ii/
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top_row = left_col = 0
        bot_row = rt_col = n-1
        cnt = 1
        op = [['']*n for index in range(n)]
        trav = 0
        while cnt <= (n*n):
            while trav <= rt_col:
                op[top_row][trav] = cnt
                cnt += 1
                trav += 1
            top_row += 1
            trav = top_row
            while trav <= bot_row:
                op[trav][rt_col] = cnt
                trav += 1
                cnt += 1
            rt_col -= 1
            trav = rt_col
            while trav >= left_col:
                op[bot_row][trav] = cnt
                trav -= 1
                cnt += 1
            bot_row -= 1
            trav = bot_row
            while trav >= top_row:
                op[trav][left_col] = cnt
                trav -= 1
                cnt += 1
            left_col += 1
            trav = left_col
        return op
