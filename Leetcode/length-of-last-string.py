# https://leetcode.com/problems/length-of-last-word/description/
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        stripped_str = s.strip()
        regexinitial = re.compile(r' ')
        regex = re.compile(r'.*? (\w+)$')
        if re.search(regexinitial,stripped_str):
            match = re.search(regex,stripped_str)
            if match:
                return len(match.group(1))
            else:
                return 0
        else:
            return len(stripped_str)