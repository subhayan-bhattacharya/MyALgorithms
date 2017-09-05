# https://leetcode.com/problems/valid-palindrome/description/
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        if len(s) == 0 or len(s) == 1:
            return True
        while start < end:
            if s[start].isalnum() and s[end].isalnum():
                if s[start].lower() != s[end].lower():
                    return False
                else:
                    end = end - 1
                    start = start + 1
            else:
                if not s[start].isalnum():
                    start = start + 1
                if not s[end].isalnum():
                    end = end - 1
        return True