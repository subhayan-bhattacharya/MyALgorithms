# https://leetcode.com/problems/add-binary/description/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        first = self.find_int_from_bin_str(a)
        second = self.find_int_from_bin_str(b)
        added_value = first + second
        bin_value = "{0:b}".format(added_value)
        return bin_value
    
        
    def find_int_from_bin_str(self,s):
        final = 0
        multiply = 0
        for i in s[::-1]:
            final += int(i) * int(2**multiply)
            multiply += 1
        return final