# https://leetcode.com/problems/zigzag-conversion/description/
# Logic : http://www.geeksforgeeks.org/print-concatenation-of-zig-zag-string-form-in-n-rows/
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        down = True
        row = 0
        matrix = [[] for i in range(numRows)]
        
        if numRows == 1:
            return s
        else:
            for letter in s:
                if row == numRows - 1:
                    down = False
                elif row == 0:
                    down = True
                matrix[row].append(letter)
                if down:
                    row = row + 1
                else:
                    row = row - 1
        final = ""
        for s in matrix:
            row_str = ''.join(s)
            final += row_str
            
        return final