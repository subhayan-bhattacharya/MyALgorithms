# https://leetcode.com/problems/array-partition-i/description/

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        start = 0
        end = len(sorted_nums) - 2
        sum = 0
        for i in range(start,end + 1,2):
            sum = sum + min(sorted_nums[i],sorted_nums[i+1])
        return sum
            