# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        first_length = len(pattern)
        second_length = len(str.split(" "))
        words = str.split(" ")
        if first_length != second_length:
            return False
        else:
            first = {}
            second = {}
            for index,key in enumerate(pattern):
                if key not in first:
                    if words[index] in second:
                        return False
                    first[key] = index
                    second[words[index]] = index
                else:
                    if words[index] not in second:
                        return False
                    if first[key] != second[words[index]]:
                        return False
                    else:
                        first[key] = index
                        second[words[index]] = index
        return True