class Solution:
       def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        check = i**2
        while check <= num:
            if check == num:
                return True
            else:
                i = i + 1
                check = i**2
        return False