# https://leetcode.com/problems/house-robber/description/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        function = []
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if i == 0:
                function.append(nums[0])
            elif i == 1:
                function.append(max(nums[0],nums[1]))
            else:
                function.append(max(function[i-1],function[i-2]+nums[i]))
        return function[-1]