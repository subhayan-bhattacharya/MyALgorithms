# https://leetcode.com/problems/longest-common-prefix/description/
# http://www.geeksforgeeks.org/longest-common-prefix-set-2-character-by-character-matching/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            prefix = []
            tobreak = 0
            new_words = sorted(strs,key=lambda s: len(s))
            for i in range(len(new_words[0])):
                letter = new_words[0][i]
                for s in new_words[1:]:
                    if s[i] != letter:
                        tobreak = 1
                        break
                if tobreak == 1:
                    break
                else:
                    prefix.append(letter)
            final_prefix = ''.join(prefix)
            return final_prefix