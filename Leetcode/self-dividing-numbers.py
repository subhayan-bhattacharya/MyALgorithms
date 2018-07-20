# https://leetcode.com/problems/self-dividing-numbers/description/

class Solution(object):
    def checkselfdividing(self,num):
        s = set()
        for digit in str(num):
            if int(digit) == 0:
                return False
            elif int(digit) == 1:
                continue
            else:
                if num % int(digit) != 0:
                    return False
        return True

        
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        final = []
        for num in range(left,right + 1):
            if num < 10:
                final.append(num)
            else:
                if self.checkselfdividing(num):
                    final.append(num)
        return final