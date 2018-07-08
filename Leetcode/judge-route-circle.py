# https://leetcode.com/problems/judge-route-circle/description/

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if moves == "":
            return True
        else:
            l_m = list(moves)
            horizontal = 0
            vertical = 0
            for move in l_m:
                if move == "U":
                    vertical = vertical + 1
                elif move == "D":
                    vertical = vertical - 1
                elif move == "R":
                    horizontal = horizontal + 1
                else:
                    horizontal = horizontal - 1
            if horizontal == 0 and vertical == 0:
                return True
            else:
                return False