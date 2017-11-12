class Solution(object):
  def countSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    n = len(s)
    if len(set(s)) == 1:
      return n * (n + 1) / 2
    # for i in xrange(2 * n - 1):
    #   l ,r = i / 2, (i + 1) / 2
    #   while l >= 0 and r < len(s) and s[l] == s[r]:
    #     l += 1
    #     r -= 1
    #     res += 1
    # return res
    return sum((i + 1) / 2 for i in self.manacher(s))

  def manacher(self, s):
    s = "^#" + "#".join(s) + "#$"
    dp = [0] * len(s)
    center, right = 0, 0
    for i in xrange(1, len(s) - 1):
      if i < right:
        dp[i] = min(right - i, dp[2 * center - i])
      while s[i + dp[i] + 1] == s[i - dp[i] - 1]:
        dp[i] += 1
      if i + dp[i] > right:
        center, right = i, i + dp[i]
    return dp