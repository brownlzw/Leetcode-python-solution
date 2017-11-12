class Solution(object):
  def findComplement(self, num):
    """
    :type num: int
    :rtype: int
    """
    n, cnt = num, 0
    while n:
      cnt += 1
      n >>= 1
    mask = (1 << cnt) - 1
    return num ^ mask
