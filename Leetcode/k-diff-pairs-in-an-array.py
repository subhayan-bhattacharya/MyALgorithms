# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_nums = sorted(nums)
        #print (sorted_nums)
        start = 0
        end = len(nums) - 1
        total = 0
        pairs = set()
        while start < end:
            diff = sorted_nums[start + 1] - sorted_nums[start]
            if diff == k:
                s = (sorted_nums[start + 1],sorted_nums[start])
                pairs.add(s)
            elif diff < k:
                next_num = start + 2
                while diff < k:
                    if next_num > end:
                        break
                    diff = sorted_nums[next_num] - sorted_nums[start]
                    if diff == k:
                        s = (sorted_nums[next_num],sorted_nums[start])
                        pairs.add(s)
                        break
                    else:
                        next_num = next_num + 1
            start = start + 1
        #print (pairs)
        return len(pairs)