class Solution(object):
  def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x < 0:
      raise ValueError("sqrt of neg")
    if x < 4:
      return 1 if x else 0
    res = 2 * self.mySqrt(x / 4)
    if (res + 1) <= x / (res + 1):
      return res + 1
    return res