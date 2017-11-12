class Solution(object):
  def maximalRectangle(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix or not matrix[0]:
      return 0
    m, n = len(matrix), len(matrix[0])
    res = 0
    h = [0] * (n + 1)
    for row in matrix:
      for i in xrange(n):
        h[i] = h[i] + 1 if row[i] == '1' else 0
      s = [-1]
      for i in xrange(n + 1):
        while h[i] < h[s[-1]]:
          cur = h[s.pop()]
          l = s[-1]
          area = cur * (i - l - 1)
          if area > res:
            res = area
        s.append(i)

    return res

