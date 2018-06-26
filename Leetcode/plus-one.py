# https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        start = 1
        output = []
        for index,key in enumerate(digits[::-1]):
            if index == 0:
                number = key
            else:
                number = number + key * (10 ** start)
                start = start + 1
        new = number + 1
        for s in str(new):
            output.append(int(s))
        return output