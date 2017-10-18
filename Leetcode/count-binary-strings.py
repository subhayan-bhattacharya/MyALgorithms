# https://leetcode.com/problems/count-binary-substrings/description/
class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        groups = []
        count = 0
        prev = s[0]
        for c in s:
            if c == prev:
                count = count + 1
            else:
                groups.append(count)
                count = 1
                prev = c
        groups.append(count)
        
        ans = 0
        
        for i in range(len(groups) - 1):
            ans = ans + min(groups[i],groups[i+1])
        return ans