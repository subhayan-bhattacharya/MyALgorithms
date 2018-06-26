# https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mappings = {}
        for var1,var2 in zip(s,t):
            if var1 in mappings:
                if mappings[var1] == var2:
                    continue
                else:
                    return False
            else:
                if var2 not in mappings.values():
                    mappings[var1] = var2
                else:
                    return False
        return True