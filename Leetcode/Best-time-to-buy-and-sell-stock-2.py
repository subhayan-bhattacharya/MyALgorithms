# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# https://www.youtube.com/watch?v=vxIMqdR8flY
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        end = len(prices) - 1
        total = 0
        for i in range(1,end + 1):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                total = total + diff
        return total