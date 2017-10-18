# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        is_same = [a == b for a,b in zip(nums,sorted_nums)]
        if all(is_same):
            return 0
        else:
            str_is_same = list(map(str,is_same))
            for index,key in enumerate(str_is_same):
                if key == "False":
                    start = index
                    break
            for i in range(len(str_is_same) - 1,-1,-1):
                if str_is_same[i] == "False":
                    end = i
                    break
        return (end - start + 1)