class Solution(object):
  def change(self, amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    dp = [1] + [0] * amount
    for coin in coins:
      for i in xrange(1, amount + 1):
        if i >= coin:
          dp[i] += dp[i - coin]
    return dp[-1]
