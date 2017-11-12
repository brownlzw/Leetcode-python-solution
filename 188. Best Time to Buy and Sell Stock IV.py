class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if  not k or len(prices) < 2:
            return 0
        if 2 * k >= len(prices):
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)
        for p in prices:
            for i in xrange(k, 0, -1):
                if buy[i] + p > sell[i]:
                    sell[i] = buy[i] + p
                if sell[i - 1] - p > buy[i]:
                    buy[i] = sell[i - 1] - p
        return sell[-1]
    # O(nk), O(k)