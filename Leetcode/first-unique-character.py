# https://leetcode.com/problems/first-unique-character-in-a-string/description/

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 0
        str_list = list(s)
        checked = []
        for index,key in enumerate(s):
            if index != len(s) - 1:
                if key not in checked:
                    if key not in str_list[index + 1:]:
                        return index
                    else:
                        checked.append(key)
                else:
                    continue
            else:
                if key not in checked:
                    return index
        return -1