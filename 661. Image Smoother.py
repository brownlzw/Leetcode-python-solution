class Solution(object):
  def imageSmoother(self, M):
    """
    :type M: List[List[int]]
    :rtype: List[List[int]]
    """
    if not M and not M[0]:
      return M
    m, n = len(M), len(M[0])
    s = [[0] * n for _ in xrange(m)]
    for i, row in enumerate(s):
      for j in xrange(n):
        row[j] = row[j - 1] if j > 0 else M[i][0]
        if j + 1 < n:
          row[j] += M[i][j + 1]
        if j - 2 >= 0:
          row[j] -= M[i][j - 2]
    for i in xrange(m):
      for j in xrange(n):
        M[i][j] = s[i][j]
        l = 0 if j == 0 else - 1
        r = 0 if j == n - 1 else 1
        top = bot = 0
        if i - 1 >= 0:
          M[i][j] += s[i - 1][j]
          top = -1
        if i + 1 < m:
          M[i][j] += s[i + 1][j]
          bot = 1
        area = (r - l + 1) * (bot - top + 1)
        M[i][j] /= area
    return M