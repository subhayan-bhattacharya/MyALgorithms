# https://leetcode.com/problems/arranging-coins/description/
class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        remain = n
        while remain >= start:
            remain = remain - start
            start = start + 1
        return start - 1