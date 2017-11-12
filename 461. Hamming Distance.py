class Solution(object):
  def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    mask = x ^ y
    res = 0
    while mask:
      mask &= mask - 1
      res += 1
    return res