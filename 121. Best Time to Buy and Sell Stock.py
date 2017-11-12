class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy = prices[0]
        profit = 0
        for stock in prices[1:]:
            if stock < buy:
                buy = stock
            elif stock - buy > profit:
                profit = stock - buy
        return profit
    # O(n), O(1)