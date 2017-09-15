# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = None
        pointer = 0
        for i in range(0,len(nums)):
            if nums[i] != prev:
                nums[pointer] = nums[i]
                pointer += 1
                prev = nums[i]
        return pointer