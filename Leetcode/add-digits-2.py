# https://leetcode.com/problems/add-digits/description/
# This is a better approach since it uses formuala
# http://burningmath.blogspot.sg/2013/09/digital-root-or-digital-sum-of-number.html

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        else:
            if num % 9 == 0:
                return 9
            else:
                return num % 9