class Solution(object):
  def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix or not matrix[0]:
      return 0
    m, n = len(matrix), len(matrix[0])
    dp = [0] * n
    for i in xrange(n):
      if matrix[0][i] == '1':
        dp[i] = 1
    max_side = 1 if any(dp) else 0
    for i in xrange(1, m):
      prev = dp[0]
      dp[0] = 1 if matrix[i][0] == '1' else 0
      if dp[0] > max_side:
        max_side = dp[0]
      for j in xrange(1, n):
        cur = 0
        if matrix[i][j] == '1':
          cur = min(prev, min(dp[j], dp[j - 1])) + 1
          if cur > max_side:
            max_side = cur
        prev = dp[j]
        dp[j] = cur
    return max_side * max_side
