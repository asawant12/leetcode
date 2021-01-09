class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = [""] * numRows
        rowNumber = 0
        direction = 1      
 
        for i in range(len(s)):  #looping through each element
            result[rowNumber] = result[rowNumber] + s[i]
            if rowNumber < numRows -1 and direction == 1:
                rowNumber += 1
            elif rowNumber > 0 and direction == -1:
                rowNumber -= 1
            else:
                direction *= -1
                rowNumber += direction
        return ''.join(result)

s = Solution()
print(s.convert("PAYPALISHIRING",3))
