class Solution(object):
  def getRow(self, rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    res = [1]
    for _ in xrange(rowIndex):
      for i in xrange(len(res) - 1, 0, -1):
        res[i] += res[i - 1]
      res.append(1)
    return res
