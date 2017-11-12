class Solution(object):
  def myPow(self, x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if not n:
      return 1
    if n < 0:
      x = 1.0 / x
      n = -n
    if n == 1:
      return x
    t = self.myPow(x, n/2)
    if (n & 1)== 0:
      return t * t
    else:
      return x * t * t

    if n < 0:
      x = 1.0 / x
      n = -n
    if not n:
      return 1
    dp = {0: x}
    res = 1
    if (n & 1) == 1:
      res = x
    for i in xrange(1, 32):
      dp[i] = dp[i - 1] * dp[i - 1]
      if n & (1 << i):
        res *= dp[i]
    return res







