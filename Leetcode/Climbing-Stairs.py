# https://leetcode.com/problems/climbing-stairs/description/
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        one_step_away = 2
        two_step_away = 1
        all_ways = 0
        for i in range(3,n+1):
            all_ways = one_step_away + two_step_away
            two_step_away = one_step_away
            one_step_away = all_ways
        return all_ways