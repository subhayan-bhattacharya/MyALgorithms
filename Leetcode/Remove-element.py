# https://leetcode.com/problems/remove-element/description/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pointer = 0
        for value in nums:
            if value != val:
                nums[pointer] = value
                pointer += 1
            else:
                continue
        return pointer