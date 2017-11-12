class Solution(object):
  def minCostII(self, costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """
    if not costs or not costs[0]:
      return 0
    n, k = len(costs), len(costs[0])
    dp = costs[0]
    for i in xrange(1, n):
      min1, min2, idx = 2147483647, 2147483647, -1
      for j in xrange(k):
        if dp[j] < min1:
          min2 = min1
          min1 = dp[j]
          idx = j
        elif dp[j] < min2:
          min2 = dp[j]
      for j in xrange(k):
        if j == idx:
          dp[j] = min2 + costs[i][j]
        else:
          dp[j] = min1 + costs[i][j]
    return min(dp)


