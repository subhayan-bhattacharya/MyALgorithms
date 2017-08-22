#Reverse an integer and return 0 if integer overflows
#https://leetcode.com/problems/reverse-integer/description/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = 0
        if x < 0:
            negative = 1
        if negative == 1:
            number = str(x)[1:]
        else:
            number = str(x)
        reverse_num = number[::-1]
        if negative == 1:
            reverse_num = "-" + reverse_num
            final_num = int(reverse_num)
        else:
            final_num = int(reverse_num)
            
        if self.checkoverflow(final_num):
            return final_num
        else:
            return 0
    
    def checkoverflow(self,number):
        import struct
        platform_c_maxint = 2 ** (struct.Struct('i').size * 8 - 1) - 1
        if not -platform_c_maxint-1 < number < platform_c_maxint:
            return False
        else:
            return True
  

    
    

