# https://leetcode.com/problems/rotate-array/description/

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) != 1:
            for i in range(k):
                last = nums.pop()
                nums.insert(0,last)