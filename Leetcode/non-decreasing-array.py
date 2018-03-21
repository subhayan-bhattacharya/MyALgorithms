class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        index = None
        length = len(nums) - 1
        for i in range(length):
            if nums[i] > nums[i+1]:
                index = i
                count = count + 1
                if count > 1:
                    return False
        if count == 0:
            return True
        else:
            if index == 0:
                return True
            after = nums[index + 1]
            before = nums[index - 1]
            if before > after:
                if (index + 1) == len(nums) - 1:
                    return True
                else:
                    if nums[index + 2] >= nums[index]:
                        return True
                    else:
                        return False
            else:
                return True