class Solution(object):
  def findLongestChain(self, pairs):
    """
    :type pairs: List[List[int]]
    :rtype: int
    """
    cur, res = float('-inf'), 0
    for p in sorted(pairs, key=lambda x: x[1]):
      if cur < p[0]:
        cur, res = p[1], res + 1
    return res

