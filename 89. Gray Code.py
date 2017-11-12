class Solution(object):
  def grayCode(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    if not n:
      return [0]
    res = self.grayCode(n - 1)
    mask = 1 << (n - 1)
    for i in xrange(len(res) - 1, -1, -1):
      res.append(res[i] | mask)
    return res

    return [i ^ i >> 1 for i in range(1 << n)]