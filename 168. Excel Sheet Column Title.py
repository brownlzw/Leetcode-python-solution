class Solution(object):
  def convertToTitle(self, n):
    """
    :type n: int
    :rtype: str
    """
    letters = "^ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n:
      res = letters[(n - 1) % 26 + 1] + res
      n = (n - 1) / 26
    return res