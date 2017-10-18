class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(nums)
        degree = max(c.values())
        first ,last = {},{}
        for index,key in enumerate(nums):
            first.setdefault(key,index)
            last[key] = index
            
        min_length = len(nums)
        for v in c:
            if c[v] == degree:
                length = last[v] - first[v] + 1
                if length < min_length:
                    min_length = length
        return min_length
                