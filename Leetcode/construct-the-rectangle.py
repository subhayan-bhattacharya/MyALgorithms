# https://leetcode.com/problems/construct-the-rectangle/description/

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        from math import sqrt
        limit = int(sqrt(area))
        i = limit
        while area % i != 0:
            i = i - 1
        if i > area // i:
            return [i,area // i]
        else:
            return [area // i,i]
                        