class Solution(object):
  def combine(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    if k > n:
      return []
    res = [[i] for i in xrange(1, n - k + 1)]
    h = n - k + 2
    for i in xrange(1, k):
      h += 1
      next = []
      for item in res:
        for j in xrange(item[-1] + 1, h):
          next.append(item + [j])
      res = next
    return res
