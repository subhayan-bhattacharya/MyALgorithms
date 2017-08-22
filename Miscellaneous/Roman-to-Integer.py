# https://leetcode.com/problems/roman-to-integer/description/
# Logic can be found here : http://www.geeksforgeeks.org/converting-roman-numerals-decimal-lying-1-3999/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number = 0
        prev = 0
        for index,letter in enumerate(s):
            if prev == 1:
                prev = 0
                continue
            else:
                if letter == "I":
                    if index != len(s) - 1:
                        if s[index+1] == "V":
                            number = number + 4
                            prev = 1
                        elif s[index+1] == "X":
                            number = number + 9
                            prev = 1
                        else:
                            prev = 0
                            number += romans[letter]
                    else:
                        number += romans[letter]
                elif letter == "X":
                    if index != len(s) - 1:
                        if s[index + 1] == "L":
                            number = number + 40
                            prev = 1
                        elif s[index + 1] == "C":
                            number = number + 90
                            prev = 1
                        else:
                            number += romans[letter]
                            prev = 0
                    else:
                        number += romans[letter]
                elif letter == "C":
                    if index != len(s) - 1:
                        if s[index + 1] == "D":
                            number = number + 400
                            prev = 1
                        elif s[index + 1] == "M":
                            number = number + 900
                            prev = 1
                        else:
                            number += romans[letter]
                            prev = 0
                    else:
                        number += romans[letter]
                else:
                    prev = 0
                    number += romans[letter]
        return number