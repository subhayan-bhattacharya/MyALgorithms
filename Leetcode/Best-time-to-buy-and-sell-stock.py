class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        minprice = sorted(prices)[-1]
        maxprice = 0
        for price in prices:
            if price < minprice:
                minprice = price
            else:
                maxprice = max(maxprice,price - minprice)
        return maxprice