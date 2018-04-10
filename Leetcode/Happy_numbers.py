# https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self,n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1:
            n = sum([int(d) * int(d) for d in str(n)])
            if n == 1:
                return True
            else:
                if n in seen:
                    return False
                else:
                    seen.add(n)
        return True