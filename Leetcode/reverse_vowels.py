#https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        final = []
        got_vowels_index = []
        for index,letter in enumerate(s):
            if letter in vowels:
                got_vowels_index.append(index)
            final.append(letter)
            
        reversed_index = list(reversed(got_vowels_index))
        for index,key in enumerate(got_vowels_index):
            final[key] = s[reversed_index[index]]
        return ''.join(final)