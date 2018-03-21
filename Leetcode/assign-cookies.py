# https://leetcode.com/problems/assign-cookies/description/
class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(s) == 0:
            return 0
        sorted_g = sorted(g,reverse=True)
        sorted_s = sorted(s,reverse=True)
        count = 0
        for i in range(0,len(sorted_g)):
            if sorted_g[i] <= sorted_s[0]:
                count = count + 1
                sorted_s.pop(0)
                if len(sorted_s) == 0:
                    return count
        return count