# https://leetcode.com/problems/add-digits/description/
# First approach using loop


class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        number = num
        while number >= 10:
            temp = 0
            while number > 0:
                temp = temp + number % 10
                number = number // 10
            number = temp
        return number