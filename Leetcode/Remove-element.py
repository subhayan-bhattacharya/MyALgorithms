# https://leetcode.com/problems/remove-element/description/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pos = 0
        val_flag = 0
        for index,element in enumerate(nums):
            if element != val:
                if val_flag == 1:
                    nums[pos] = element
                    pos = pos + 1
                else:
                    pos = pos + 1
            else:
                val_flag = 1
        return pos