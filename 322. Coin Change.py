class Solution(object):
  def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    coins.sort(reverse=True)
    lenc, self.res = len(coins), 2 ** 31 - 1

    def dfs(pt, rem, count):
      if not rem:
        self.res = min(self.res, count)
      for i in xrange(pt, lenc):
        if coins[i] <= rem <= coins[i] * (self.res - count):
          dfs(i, rem - coins[i], count + 1)

    for i in xrange(lenc):
      dfs(i, amount, 0)

    return self.res if self.res < 2 ** 31 - 1 else -1