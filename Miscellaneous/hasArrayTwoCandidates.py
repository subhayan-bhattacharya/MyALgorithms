# Given an array A[] and a number x, check for pair in A[] with sum as x
# http://www.geeksforgeeks.org/write-a-c-program-that-given-a-set-a-of-n-numbers-and-another-number-x-determines-whether-or-not-there-exist-two-elements-in-s-whose-sum-is-exactly-x/
# Leetcode problem : https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        sorted_nums = sorted(nums)
        start = 0
        end = len(sorted_nums) - 1
        while start < end:
            sum = sorted_nums[start] + sorted_nums[end]
            if sum == target:
                if sorted_nums[start] == sorted_nums[end]:
                    positions = [i for i,x in enumerate(nums) if x == sorted_nums[start]]
                    result.extend(positions)
                else:
                    result.append(nums.index(sorted_nums[start]))
                    result.append(nums.index(sorted_nums[end]))
                return result
            elif sum < target:
                start = start + 1
            elif sum > target:
                end = end - 1