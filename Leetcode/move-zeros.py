# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = len(nums)
        to_break = False
        for i in range(start,end):
            if nums[i] == 0:
                if i == end - 1:
                    break
                else:
                    for j in range(i,end):
                        if nums[j] != 0:
                            nums[i] = nums[j]
                            nums[j] = 0
                            if j == end - 1:
                                to_break = True
                            break
            if to_break:
                break