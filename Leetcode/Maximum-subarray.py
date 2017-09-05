# https://leetcode.com/problems/maximum-subarray/description/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far =nums[0]
        curr_max = nums[0]
        size = len(nums)
        for i in range(1,size):
            curr_max = max(nums[i], curr_max + nums[i])
            max_so_far = max(max_so_far,curr_max)
         
        return max_so_far