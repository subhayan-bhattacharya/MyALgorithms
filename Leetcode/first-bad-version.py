# https://leetcode.com/problems/first-bad-version/description/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        mid = int(start + (end - start)/2)
        while True:
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    end = mid - 1
                    mid = int(start + (end - start)/2)
            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                else:
                    start = mid
                    mid = int(start + (end - start)/2)