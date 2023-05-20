# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def fill_row(row_num, prev_row):
            row = [1]
            if row_num <=1:
                if row_num != 0:
                    row.append(1)
                return row
            else:
                left=0
                right=1
                while right < len(prev_row):
                    new_val = prev_row[left] + prev_row[right]
                    left += 1
                    right += 1
                    row.append(new_val)
                row.append(1)
            return row
        pascal_triangle = []
        prev_row = -1
        for row in range(numRows):
            row = fill_row(row, prev_row)
            pascal_triangle.append(row)
            prev_row = row
        return pascal_triangle
    
                    
