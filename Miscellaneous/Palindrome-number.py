# https://leetcode.com/problems/palindrome-number/description/


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            number = x
            str_number = str(number)
            reverse = []
            while number >= 1:
                reverse.append(str(number % 10))
                number = number // 10
            if len(reverse) == 0:
                reversed_num = "0"
            else:
                reversed_num = ''.join(reverse)
            if reversed_num == str_number:
                return True
            else:
                return False