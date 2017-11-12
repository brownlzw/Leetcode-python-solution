class Solution(object):
  def nearestPalindromic(self, n):
    """
    :type n: str
    :rtype: str
    """
    l = len(n)
    if l == 1:
      return str(int(n) - 1)
    # with different digits width, it must be either 10...01 or 9...9
    candidates = set(("1" + "0" * (l - 1) + "1", "9" * (l - 1)))  # SEE PERFORMANCE BELOW
    # the closest must be in middle digit +1, 0, -1, then flip left to right
    prefix = int(n[:(l + 1) / 2])
    for i in map(str, (prefix - 1, prefix, prefix + 1)):
      if l & 1:
        candidates.add(i + i[:-1][::-1])
      else:
        candidates.add(i + i[::-1])
    candidates.discard(n)
    return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))