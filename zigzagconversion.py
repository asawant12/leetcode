class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        index=0
        matrix = []
        fin_answer=""
        row_str=""
        for row_index in range(numRows):
            matrix.append([])

        col_index = 0
        letter_index = 0
        while index < len(s):
            row_index = 0
            if letter_index == 0:
                while row_index < numRows:
                    matrix[row_index].append(s[index])
                    row_index += 1
                    index += 1
                    if index >= len(s):
                        break
                col_index += 1
                letter_index = numRows-2
            else:
                while row_index < numRows:
                    if row_index == letter_index:
                        matrix[row_index].append(s[index])
                        index += 1
                        if index >= len(s):
                            break
                    else:
                        matrix[row_index].append("")
                    row_index += 1
                col_index += 1
                letter_index -= 1
        for rows in matrix:
           row_str = "".join(rows)
           fin_answer +=  row_str
        return fin_answer
            
