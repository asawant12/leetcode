# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumt = 0
        for index in range(len(mat[0])):
            sumt = sumt + mat[index][index]
            mat[index][index] = -1
        index = len(mat[0])-1
        row =0
        while index >= 0:
            if mat[row][index] != -1:
                sumt = sumt + mat[row][index]
            index -= 1
            row+= 1
        return sumt
