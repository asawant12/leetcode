#Given a binary matrix mat[][] containing 0’s and 1’s. Each row of the matrix is sorted in the non-decreasing order, the task is to find the 
#left-most column of the matrix with at least one 1 in it.
#Note: If no such column exists return -1.

matrix1 = [[0, 0, 0, 1,0],
          [0, 0, 1, 1,0],
          [0, 1, 1, 1,0],
          [0, 0, 0, 0,0]]

matrix2 = [[0, 0, 0, 0,0],
          [0, 0, 0, 0,0],
          [0, 0, 0, 0,0],
          [0, 0, 0, 0,0]]

matrix3 = [[1, 0, 0, 0,0],
          [0, 1, 0, 0,0],
          [0, 0, 1, 0,0],
          [0, 0, 0, 1,0]]

def test_matrix(matrix):
  row_index = 0
  col_index = len(matrix)-1
  col = -1
  while col_index >= 0:
    for row_index in range(len(matrix)):
      if matrix[row_index][col_index] == 1:
          col = col_index + 1
          break
    col_index -= 1
  return col
for mat in (matrix1, matrix2, matrix3):
  print(test_matrix(mat))
